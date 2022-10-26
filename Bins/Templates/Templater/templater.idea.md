<%*
//v1.4: Adding option for including a header for each DNP day to fold

//Name of the Quick Capture file. Do NOT include extension '.md'
let idea = await tp.system.prompt("Enter a Idea");
let qcFileName = "💥 " + idea

//Leave this blank if you want to use the default file path location (set to '/' to use root of vault)
//let folderOverride = '/Spaces/Daily/';
let folderOverride = '/Spaces/Ideas/';

let qcFolderLocation;
if(folderOverride) {
    qcFolderLocation = folderOverride;
} else {
    if(this.app.vault.config.newFileLocation != 'current') {
        qcFolderLocation = this.app.fileManager.getNewFileParent().path;
    } else {
        qcFolderLocation = '/';
    }
}
if(qcFolderLocation != ''){qcFolderLocation = qcFolderLocation + '/'}
qcFolderLocation = qcFolderLocation.replace(/\/\//g,'/');
if(qcFolderLocation == '/'){qcFolderLocation = ''}
if(qcFolderLocation.startsWith('/')){qcFolderLocation = qcFolderLocation.substring(1)}

let qcFilePath = qcFolderLocation + qcFileName + '.md';
let qcFile = this.app.vault.getAbstractFileByPath(qcFilePath);
if(!qcFile) {
    qcFile = await this.app.vault.create(qcFilePath, '');
}

if(qcFile) {
    let finalNote = idea;
    let curContent = await this.app.vault.read(qcFile);
    let newContents;
    newContents = "---\ntitle: " + qcFileName + "\ncreated: " + tp.date.now("YYYY-MM-DD") + "\nresolve: \ntags:\n  - 'ideas'\n  - 'created/" + tp.date.now("YYYY/MMM/DD") + "'\n---\n\n"+ finalNote + '\n' + curContent

    this.app.vault.modify(qcFile, newContents);
}
%>
[[<%* tR += qcFileName %>]]