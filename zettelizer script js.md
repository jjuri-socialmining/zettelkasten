zettelizer script js là một macro dùng để tách các header lelel 3 của một file note thành những file note riêng biệt.

https://quickadd.obsidian.guide/docs/Examples/Macro_Zettelizer

## Original
```js
module.exports = async e => {
    console.log("Starting..."), console.log(e);
    const o = e.app.workspace.getActiveFile();
    if (!o) return void new Notice("No active file.");
    console.log("Found active file: ", o.basename);
    const a = e.app.metadataCache.getFileCache(o).headings;
    if (!a) return void new Notice(`No headers in file ${o.name}`);
    console.log("Found headings in active file: ", a);
    const i = "Reference_Box/Zettels";
    e.app.vault.adapter.exists(i) ? (console.log("Folder does exist: ", i), a.forEach((async a => {
        if (console.log(`Checking ${a.heading}. It is level ${a.level}`), 3 === a.level) {
            const t = a.heading.split(" "),
                l = t[0].trim(),
                n = t.length > 1 ? [...t.slice(1)].join(" ").trim() : "",
                s = `${i}/${n.replace(/[\\,#%&\{\}\/*<>$\'\":@]*/g,"")}.md`,
                c = `![[${o.basename}#${l}${n?" "+n:""}]]`;
            console.log(`Path: ${s}.\nContent: ${c}`), n && !await e.app.vault.adapter.exists(s) ? await e.app.vault.create(s, c) : n && new Notice(`File ${s} already exists.`, 5e3)
        }
    })), console.log("Finished!")) : new Notice(`Could not find folder ${i}`)
};
```
## Add time stamp prefix in filename
 ```js
	const date = window.moment().format("YYYYMMDD");
```
```js
module.exports = async e => {
    console.log("Starting..."), console.log(e);
	const date = window.moment().format("YYYYMMDD ");
    const o = e.app.workspace.getActiveFile();
    if (!o) return void new Notice("No active file.");
    console.log("Found active file: ", o.basename);
    const a = e.app.metadataCache.getFileCache(o).headings;
    if (!a) return void new Notice(`No headers in file ${o.name}`);
    console.log("Found headings in active file: ", a);
    const i = "Reference_Box/Zettels";
    e.app.vault.adapter.exists(i) ? (console.log("Folder does exist: ", i), a.forEach((async a => {
        if (console.log(`Checking ${a.heading}. It is level ${a.level}`), 3 === a.level) {
            const t = a.heading.split(" "),
                l = t[0].trim(),
                n = t.length > 1 ? [...t.slice(1)].join(" ").trim() : "",
                s = `${i}/${date}${n.replace(/[\\,#%&\{\}\/*<>$\'\":@]*/g,"")}.md`,
                c = `![[${o.basename}#${l}${n?" "+n:""}]]`;
            console.log(`Path: ${s}.\nContent: ${c}`), n && !await e.app.vault.adapter.exists(s) ? await e.app.vault.create(s, c) : n && new Notice(`File ${s} already exists.`, 5e3)
        }
    })), console.log("Finished!")) : new Notice(`Could not find folder ${i}`)
};
```
Promp
    const {
        quickAddApi: { inputPrompt },
    } = params;

```js
module.exports = async e => {
    // Object destructuring. We pull inputPrompt out of the QuickAdd API in params.
    const {
        quickAddApi: { inputPrompt },
    } = params;
    const book_prefix = await inputPrompt("Prefix of quote\nExample: Hồi ký Nguyễn Hiến Lê -> HKNHL");
    console.log("Starting..."), console.log(e);
	const date = window.moment().format("YYYYMMDD ");
    const o = e.app.workspace.getActiveFile();
    if (!o) return void new Notice("No active file.");
    console.log("Found active file: ", o.basename);
    const a = e.app.metadataCache.getFileCache(o).headings;
    if (!a) return void new Notice(`No headers in file ${o.name}`);
    console.log("Found headings in active file: ", a);
    const file_path = "Reference_Box/Zettels";book_prefix
    e.app.vault.adapter.exists(file_path) ? (console.log("Folder does exist: ", file_path), a.forEach((async a => {
        if (console.log(`Checking ${a.heading}. It is level ${a.level}`), 3 === a.level) {
            const t = a.heading.split(" "),
                l = t[0].trim(),
                n = t.length > 1 ? [...t.slice(1)].join(" ").trim() : "",
                s = `${file_path}/${book_prefix}${n.replace(/[\\,#%&\{\}\/*<>$\'\":@]*/g,"")}.md`,
                c = `![[${o.basename}#${l}${n?" "+n:""}]]`;
            console.log(`Path: ${s}.\nContent: ${c}`), n && !await e.app.vault.adapter.exists(s) ? await e.app.vault.create(s, c) : n && new Notice(`File ${s} already exists.`, 5e3)
        }
    })), console.log("Finished!")) : new Notice(`Could not find folder ${i}`)
};
```