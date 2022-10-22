#!groovy

def linux_agent = 'las-sw-03'
def windows_agent = 'las-win7-03'
def project_name = "spica5"
def target_dir = "/home/swott-jenkins/public_html/projects"

// Don't change
def g_fw_version_num = params.FW_VERSION
def g_api_version_num = params.API_VERSION

pipeline {
    agent none

    environment {
        //EMAIL_TO = "ngnguyen@marvell.com,nthuy@marvell.com,ldinh@marvell.com,rfuriato@marvell.com,fvanetti@marvell.com,sgaiotto@marvell.com"
        EMAIL_TO = "ngnguyen@marvell.com"
    }
    
    options {
        timeout(time: 2, unit: 'HOURS') 
    }

    stages {
        stage ("Linux") {
            // For fast debug
            when { expression { return true }}

            agent { label linux_agent}

            environment {
                PATH = "/tools/cad/python3.9.12/bin:/tools/cad/anaconda3/2019.03/Linux/2019.03/bin:/tools/cad/sifive/FreedomStudio/4.18.0/Linux/SiFive/riscv64-unknown-elf-toolchain-10.2.0-2020.12.8/bin:${PATH}"
            }

            stages {
                stage ("Prerequisites") {
                    parallel {
                        stage ("Check build tools") {
                            steps {
                                sh """
                                which meson
                                meson --version
                                which ninja
                                ninja --version
                                which python
                                python --version
                                which gcc
                                gcc --version
                                which g++
                                g++ --version
                                which swig
                                swig -version
                                """
                            }
                        }
                    }
                }

                stage ("Setup workspace") {
                    parallel {
                        stage ("spica5.git") {
                            steps {
                                dir ("${env.WORKSPACE}/hsc") {
                                    echo "Trying to checkout branch ${params.BUILD_FROM}"
                                    retry(5) {
                                        gitLabCheckout([repoUrl: 'git@las-gitlab:hsc/spica5.git',
                                                        branch: "${params.BUILD_FROM}",
                                                        relativeTargetDir: 'spica5'])
                                    }
                                }
                            }
                        }

                        stage ("bin.git") {
                            steps {
                                dir (env.WORKSPACE) {
                                    retry(5) {
                                        gitLabCheckout([repoUrl: 'git@las-gitlab:hsc/bin.git', 
                                                        branch: "refs/heads/master",
                                                        relativeTargetDir: 'bin'])
                                    }
                                }
                            }
                        }

                        stage ("3rdparty.git") {
                            steps {
                                dir (env.WORKSPACE) {
                                    retry(5) {
                                        gitLabCheckout([repoUrl: 'git@las-gitlab:hsc/3rdparty.git', 
                                                        branch: "refs/heads/master",
                                                        relativeTargetDir: '3rdparty'])
                                    }
                                }
                            }
                        }
                    }
                }

                stage ("Update FW version") {
                    when { expression { return params.FW_BUILD } }
                    steps {
                        dir ("${env.WORKSPACE}/hsc/${project_name}/firmware/application") {
                            sh "./application_fw_tag.sh"
                        }

                        dir ("${env.WORKSPACE}/hsc/${project_name}/firmware/application") {
                            script {
                                g_fw_version_num = sh (script: "make -f version.inc version_num", returnStdout: true).trim()
                            }
                        }
                    }
                }

                stage ("FW Builds") {
                    when { expression { return params.FW_BUILD } }
                    parallel {
                        stage ("FW RISC-V") {
                            steps {
                                dir ("${env.WORKSPACE}/hsc/${project_name}/firmware/application") {
                                    sh "./application_fw_build.sh"
                                }
                            }
                        }

                        stage ("FW Components") {
                            steps {
                                dir ("${env.WORKSPACE}/hsc/${project_name}/firmware/application") {
                                    echo "TODO: Not implemented"
                                }
                            }
                        }
                    }
                }

                stage ('Release FW') {
                    when { expression { return params.FW_BUILD } }
                    steps {
                        dir ("${env.WORKSPACE}/hsc/${project_name}/firmware/application") {
                            sh "./application_fw_rls.sh ${target_dir}"
                        }
                    }
                }

                stage ("Update API version") {
                    when { expression { return params.API_BUILD } }
                    steps {
                        dir ("${env.WORKSPACE}/hsc/${project_name}/api/capi") {
                            sh "./api_tag.sh"
                        }
                        dir ("${env.WORKSPACE}/hsc/${project_name}/api/capi") {
                            script {
                                g_api_version_num = sh (script: "make version_num", returnStdout: true).trim()
                            }
                        }
                    }
                }
                
                stage ("C-API SKUs") {
                    when { expression { return params.API_BUILD } }
                    steps {
                        script {
                            artifacts_dir="${env.WORKSPACE}/hsc/${project_name}/api_skus"
                            artifacts_dir_api="${artifacts_dir}/api"

                            dir ("${env.WORKSPACE}/hsc/${project_name}/api/capi") {
                                sh "./api_build_skus.sh 3.9 ${artifacts_dir_api}"
                            }

                            dir ("${artifacts_dir}") {
                                archiveArtifacts artifacts: 'api/**/*', fingerprint: false
                                echo "Archived API SKUs to build artifacts"
                            }

                            sh "rm -rf ${artifacts_dir}"
                        }   
                    }
                }
            } // End of Pipeline stages
        }

        stage ('Windows') {
            // For fast debug
            when { expression { return params.API_BUILD } }

            agent { label windows_agent }

            stages {
                stage ("Setup workspace") {
                    parallel {
                        stage ("spica5.git") {
                            steps {
                                dir ("${env.WORKSPACE}/hsc") {
                                    echo "Trying to checkout branch ${params.BUILD_FROM}"
                                    retry(5) {
                                        gitLabCheckout([repoUrl: 'git@las-gitlab:hsc/spica5.git',
                                                        branch: "${params.BUILD_FROM}",
                                                        relativeTargetDir: 'spica5'])
                                    }
                                }
                            }
                        }

                        stage ("bin.git") {
                            steps {
                                dir (env.WORKSPACE) {
                                    retry(5) {
                                        gitLabCheckout([repoUrl: 'git@las-gitlab:hsc/bin.git', 
                                                        branch: "refs/heads/master",
                                                        relativeTargetDir: 'bin'])
                                    }
                                }
                            }
                        }

                        stage ("3rdparty.git") {
                            steps {
                                dir (env.WORKSPACE) {
                                    retry(5) {
                                        gitLabCheckout([repoUrl: 'git@las-gitlab:hsc/3rdparty.git', 
                                                        branch: "refs/heads/master",
                                                        relativeTargetDir: '3rdparty'])
                                    }
                                }
                            }
                        }
                    }
                }

                stage ("Build API python") {
                    steps {
                        script {
                            dir ("${env.WORKSPACE}/hsc/${project_name}/api/capi") {
                                artifacts_dir="${env.WORKSPACE}\\hsc\\${project_name}\\spica5_py39_32bit"
                                artifacts_dir_api="${artifacts_dir}\\api"
                                bat "api_python_wrapper_win32.bat 3.9 ${artifacts_dir_api}"

                                // Archive to artifacts
                                dir ("${artifacts_dir}") {
                                    archiveArtifacts artifacts: 'api/**/*', fingerprint: false
                                }

                                bat """
                                REM Clean workspace
                                rmdir /s /q ${artifacts_dir}
                                echo "Cleaned workspace %cd% done"
                                """
                            }
                        }

                        script {
                            dir ("${env.WORKSPACE}/hsc/${project_name}/api/capi") {
                                artifacts_dir="${env.WORKSPACE}\\hsc\\${project_name}\\spica5_py39_64bit"
                                artifacts_dir_api="${artifacts_dir}\\api"
                                bat "api_python_wrapper_win64.bat 3.9 ${artifacts_dir_api}"

                                // Archive to artifacts
                                dir ("${artifacts_dir}") {
                                    archiveArtifacts artifacts: 'api/**/*', fingerprint: false
                                }

                                bat """
                                REM Clean workspace
                                rmdir /s /q ${artifacts_dir}
                                echo "Cleaned workspace %cd% done"
                                """
                            }
                        }
                    }
                }
            }
        }

        stage ('Release') {
            agent { label linux_agent }

            environment {
                FW_ARTIFACTS_URL = "${env.BUILD_URL}/artifact/fw"
                API_ARTIFACTS_URL = "${env.BUILD_URL}/artifact/api"
                FW_TARGET_DIR = "${target_dir}/${project_name}/firmware/application/${env.BUILD_TYPE}/${g_fw_version_num}"
                API_TARGET_DIR = "${target_dir}/${project_name}/api/${env.BUILD_TYPE}/${g_api_version_num}"
                UAPI_TARGET_DIR = "${target_dir}/${project_name}/uapi/${env.BUILD_TYPE}/${g_api_version_num}"
            }

            stages {
                stage ('Release API') {
                    when { expression { return params.API_BUILD } }
                    steps {
                        script {
                            // Build UAPI package
                            u_api_release_dir = release_dir_allocate([target_dir: "${env.UAPI_TARGET_DIR}"])
                            echo "Buiding UAPI package version ${g_api_version_num} to ${u_api_release_dir}"
                            dir ("${env.WORKSPACE}") {
                                sh "hsc/${project_name}/api/capi/api_publish_release.sh ${env.API_ARTIFACTS_URL} ${env.UAPI_TARGET_DIR} uapi"
                            }

                            // Build API package
                            api_release_dir = release_dir_allocate([target_dir: "${env.API_TARGET_DIR}"])
                            echo "Buiding CAPI package version ${g_api_version_num} to ${api_release_dir}"
                            dir ("${env.WORKSPACE}") {
                                sh "hsc/${project_name}/api/capi/api_publish_release.sh ${env.API_ARTIFACTS_URL} ${env.API_TARGET_DIR} api"
                            }
                        }
                    }
                }

                stage ('Release GUI') {
                    when { expression { return params.GUI_BUILD } }
                    steps {
                        dir ("${env.WORKSPACE}/hsc/${project_name}/bin/jenkins") {
                            sh "./gui_release_proc.sh ${g_fw_version_num} ${g_api_version_num}"
                        }
                    }
                }
            }
        }
    }

    post {
        failure {
            emailext(to: "${env.EMAIL_TO}",
                subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                body: "OPPS!!! The build ${env.RUN_DISPLAY_URL} is FAILED")
            updateGitlabCommitStatus(name: 'Jenkins', state: 'failed')
            addGitLabMRComment(comment: '[From Jenkins] Build is fail')
        }

        aborted {
            emailext(to: "${env.EMAIL_TO}",
                subject: "Aborted Pipeline: ${currentBuild.fullDisplayName}",
                body: "OPPS!!! The build ${env.RUN_DISPLAY_URL} is ABORTED")
            updateGitlabCommitStatus(name: 'Jenkins', state: 'canceled')
            addGitLabMRComment(comment: '[From Jenkins] Build is aborted')
        }

        unstable {
            emailext(to: "${env.EMAIL_TO}",
                subject: "Unstable Pipeline: ${currentBuild.fullDisplayName}",
                body: "The build ${env.RUN_DISPLAY_URL} is SUCCEEDED but having some failures. Please check Jenkins report for more detail")
            updateGitlabCommitStatus(name: 'Jenkins', state: 'success')
            addGitLabMRComment(comment: '[From Jenkins] Build is unstable, some tests may be failed or lower source code coverage. Please check Jenkins report')
        }

        success {
            emailext(to: "${env.EMAIL_TO}",
                    subject: "Success Pipeline: ${currentBuild.fullDisplayName}",
                    body: "The build ${env.RUN_DISPLAY_URL} is SUCCEEDED and release done")
            updateGitlabCommitStatus(name: 'Jenkins', state: 'success')
            addGitLabMRComment(comment: '[From Jenkins] Build is good')
        }
    }
}

def gitLabCheckout(Map info) {
    checkout([$class: 'GitSCM',
               branches: [[name: info["branch"]]],
               doGenerateSubmoduleConfigurations: false,
               extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: info["relativeTargetDir"]],
                            [$class: 'CloneOption', timeout: 60],
                            [$class: 'SubmoduleOption',
                             disableSubmodules: false,
                             parentCredentials: true,
                             recursiveSubmodules: true,
                             reference: '',
                             threads: 5,
                             trackingSubmodules: false]],
                             submoduleCfg: [],
                             userRemoteConfigs: [[
                                credentialsId: '92665dca-cf26-4324-922b-88bfc40ff944',
                                url: info["repoUrl"]]]])
}

def release_dir_allocate(Map info) {
    // target_dir
    target_dir = info["target_dir"]

    allocated_release_dir = sh (script: """
    i=1
    release_dir=${target_dir}
    while [ -d \$release_dir ]; do
        release_dir=${target_dir}_\$i
        i=\$((i+1))
    done
    echo \$release_dir
    """, returnStdout: true). trim()

    echo "Allocated an empty directory ${allocated_release_dir}"
    return allocated_release_dir
}
