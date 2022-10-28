<%*
//v1.4: Adding option for including a header for each DNP day to fold

//Name of the Quick Capture file. Do NOT include extension '.md'
let qcFileName = tp.date.now("$ YYMMDD - ");
let tag_created = "created/" + tp.date.now("YYYY/MMM/DD");

//Leave this blank if you want to use the default file path location (set to '/' to use root of vault)
//let folderOverride = '/Spaces/Daily/';
let folderOverride = '/Spaces/Tasks/';

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

let qcNote = await tp.system.prompt("In put task name");
let qcFilePath = qcFolderLocation + qcFileName + qcNote + '.md';
let qcFile = this.app.vault.getAbstractFileByPath(qcFilePath);
if(!qcFile) {
    qcFile = await this.app.vault.create(qcFilePath, '');
}

if(qcFile) {
    type = await tp.system.suggester(["Inbox", "Someday", "Todo"], ["'tasks/inbox'", "'tasks/someday'", "'tasks/todo'"]);

	let descrip = await tp.system.prompt("Description");
    let finalNote =  finalTimestamp + qcNote;
    let curContent = await this.app.vault.read(qcFile);
    let newContents;
    newContents = '---\ntitle: ' + qcNote + "\ntags:\n  - '" + tag_created + "'\n" + "  - " + type + "\nis_done: False\n---\n\n## Notes:\n" +  descrip;

    this.app.vault.modify(qcFile, newContents);
}
%>- [ ] [[<%* tR += qcFileName + qcNote %>]] #tasks/todo 
