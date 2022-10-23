<%*
//v1.4: Adding option for including a header for each DNP day to fold

//'first' will add to top of file. 'last' will add to bottom of file
let firstOrLastLine = 'last';

//Name of the Quick Capture file. Do NOT include extension '.md'
let qcFileName = tp.date.now("❔YYMMDD-HHmm");


//Leave this blank if you want to use the default file path location (set to '/' to use root of vault)
//let folderOverride = '/Spaces/Daily/';
let folderOverride = '/Spaces/Quiz/';

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
if(!qcFile) {
    qcFile = await this.app.vault.create(qcFilePath, '');
}

if(qcFile) {
    let qcNote = await tp.system.prompt("Enter a Quiz");
	let answer_Note = await tp.system.prompt("Enter Answers");
    let isTodo = qcNote.startsWith(';');
    let finalNote = (isTodo ? '- [ ] ' : '') + finalTimestamp + (isTodo ? qcNote.substring(1) : qcNote);
    let curContent = await this.app.vault.read(qcFile);
    let newContents;
    if(firstOrLastLine == 'last'){newContents = curContent + '\n\n#quiz❔: ' + finalNote + '\n?\n' + answer_Note + '\n\n'}
    else {
        if(bAddHeader) {
            let curDateHeader = '# ' + curDateFormat;
            curContent = curContent.replace('\n' + curDateHeader + '\n\n', '');
            newContents = '\n' + curDateHeader + '\n\n' + finalNote + '\n' + curContent;
        } else {
            newContents = finalNote + '\n' + curContent
        }
    }
    this.app.vault.modify(qcFile, newContents);
}
%>
[[<%* tR += qcFileName %>]]