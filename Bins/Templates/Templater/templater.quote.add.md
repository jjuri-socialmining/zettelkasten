<%*
//v1.4: Adding option for including a header for each DNP day to fold

//Name of the Quick Capture file. Do NOT include extension '.md'
let qcFileName = tp.date.now("💬YYMMDD-HHmmss");
let tag_created = "created/" + tp.date.now("YYYY/MMM/DD");

//Leave this blank if you want to use the default file path location (set to '/' to use root of vault)
//let folderOverride = '/Spaces/Daily/';
let folderOverride = '/Reference_Box/Quotes/';

//Add a header for each day to nest the quick capture notes under (only works when firstOrLastLine = 'first')
let bAddHeader = false;

let curDateFormat = '';
let finalTimestamp = curDateFormat;
let curTimeFormat = '';
if(curTimeFormat != ''){finalTimestamp = finalTimestamp + ' ' + curTimeFormat}

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
qcFile = await this.app.vault.create(qcFilePath, '');

if(qcFile) {
	let Quote = await tp.system.prompt("Quote");
	let source = await tp.system.prompt("Nguồn: Tác giả, sách, link...");
    let curContent = await this.app.vault.read(qcFile);
    let newContents;
    newContents = '---\ntitle: ' + qcFileName + "\ntags:\n  - '" + tag_created + "'\n  - "  + "'quotes'\nsource:\n  - " + source +"\n---\n\n## Notes:\n" + Quote + "\n\nSource: " + source + "\n\n## Ideas & thoughts:\n";

    this.app.vault.modify(qcFile, newContents);
}
%>
[[<%* tR += qcFileName %>]]