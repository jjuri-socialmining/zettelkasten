<%*
let sourceName = (tp.file.title); 
let n = sourceName.length; 
let pathName = (tp.file.path (relative = true));
let firstOut = pathName.slice(0,-(n+4));
let firstPos = firstOut.indexOf("/");
	if (firstPos ==-1) {;
		let systems = firstOut.startsWith("~000");
		if (systems ==true){;
		tR += "[[";
		tR += firstOut;
		tR += "]] >>";
		}else{;
		tR += "[[";
		tR += firstOut;
		tR += "]] >>"};
	}else{;
		while (firstPos !==-1){;
			let remainderPos = firstOut.indexOf("/");
			if (remainderPos==-1){remainderPos = firstOut.length};
			let out = firstOut;
			let indexPrefix = ""
			let remainderLess = firstOut.slice(0,(remainderPos));
			remainderLess = indexPrefix.concat(remainderLess);
			if (remainderLess ==(tp.file.title)){break};
			tR += "[[";
			tR += remainderLess;
			tR += "]] >> ";
			firstPos = out.indexOf("/");
			firstOut = out.slice(firstPos+1);
	}};
%>
