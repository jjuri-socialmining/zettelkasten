module.exports = async e => {
    // Object destructuring. We pull inputPrompt out of the QuickAdd API in params.
    const {
        quickAddApi: { inputPrompt },
    } = e;
    const book_prefix = await inputPrompt("Prefix of quote (Ex: Hồi ký Nguyễn Hiến Lê -> HKNHL)");
	const tag = await inputPrompt("tags: quote/*");
    console.log("Starting..."), console.log(e);
    const o = e.app.workspace.getActiveFile();
    if (!o) return void new Notice("No active file.");
    console.log("Found active file: ", o.basename);
    const a = e.app.metadataCache.getFileCache(o).headings;
    if (!a) return void new Notice(`No headers in file ${o.name}`);
    console.log("Found headings in active file: ", a);
    const file_path = "Reference_Box/Zettels";
    e.app.vault.adapter.exists(file_path) ? (console.log("Folder does exist: ", file_path), a.forEach((async a => {
        if (console.log(`Checking ${a.heading}. It is level ${a.level}`), 3 === a.level) {
            const t = a.heading.split(" "),
                pos = t[0].trim(), // position start by p21 (page 21) or l43 (location/loc 43)
                n = t.length > 1 ? [...t.slice(1)].join(" ").trim() : "",
                s = `${file_path}/${book_prefix}, ${pos} - ${n.replace(/[\\,#%&\{\}\/*<>$\'\":@]*/g,"")}.md`,
                c = `---\ncssclass: quote\n---\n#quote/${tag}\n![[${o.basename}#${pos}${n?" "+n:""}]]\n\nsource:: [[${o.basename}]], ${pos}`;
            console.log(`Path: ${s}.\nContent: ${c}`), n && !await e.app.vault.adapter.exists(s) ? await e.app.vault.create(s, c) : n && new Notice(`File ${s} already exists.`, 5e3)
        }
    })), console.log("Finished!")) : new Notice(`Could not find folder ${i}`)
};