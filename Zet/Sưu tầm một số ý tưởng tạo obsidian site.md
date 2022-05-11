---
title: Sưu tầm một số ý tưởng tạo obsidian
UID: 210921211247
created: 21-Sep-2021
tags:
  - 'created/2021/Sep/21'
  - 'garden'
  - 'permanent/concept'
publish: False
---
# Sưu tầm một số ý tưởng tạo obsidian

## Notes:
- [[Joschuasgarden]] - https://joschuasgarden.com/: 
	- Trang dùng [[Obsidian]] để tạo những trích dẫn, tham khảo [[Kinh thánh]]
	- Tham khảo thêm hướng dẫn trên [obsidian forum](https://forum.obsidian.md/t/bible-study-in-obsidian-kit-including-the-bible-in-markdown/12503?u=joschua)
	- Bản dịch các ngôn ngữ ở trên trang [kinh thánh gateway](https://www.biblegateway.com/versions/Vietnamese-Bible-Easy-to-Read-Version-BPT/#booklist), tool sẽ download bản dịch tương ứng với câu lệnh
	- Trên trang gateway có [[Các bản dịch tiếng Việt Kinh Thánh trên BibleBateway]]:  ^2385af
		- BD2011: Bản dịch 2011
		- NVB: New Vietnamese Bible
		- BPT: [[Vietnamese Bible Easy-To-Read Version]]
	- Cách cài đặt, download thánh kinh ra md, tham khảo [hướng dẫn](https://github.com/mkudija/BibleGateway-to-Obsidian-Catholic)
		- vào link github, clone https://github.com/selfire1/BibleGateway-to-Obsidian
		```
	 	git clone https://github.com/selfire1/BibleGateway-to-Obsidian.git
	 	cd BibleGateway-to-Obsidian
	 	git submodule init
	 	git submodule update
		```
	 	- Copy `bg2obs.sh` và file `bg2md.rb` của submodule vào chung 1 folder
	 	- Install `ruby` trên windows, rồi install `gem`, dùng gem install một số library
		```
		gem install colorize optparse clipboard
		```
		- Mở mingwin/gitbash lên và run `bash bg2obs.sh -i -v BPT`
			- BPT là một phiên bản tiếng việt [[#^2385af]], lưu ý, trong khi download không nên can thiệp vào clipboard
- [[Quartz template]]
- [[Blue book template]]
- [https://github.com/MaggieAppleton/digital-gardeners](https://github.com/MaggieAppleton/digital-gardeners)
- https://simply-jekyll.netlify.app/posts/introduction-to-simply-jekyll
	- https://github.com/raghudotcc/simply-jekyll
- https://www.mentalnodes.com/the-only-way-to-learn-in-public-is-to-build-in-public
- https://github.com/binyamin/eleventy-garden
	- ![[Pasted image 20220501215628.png]]
- https://github.com/mathieudutour/gatsby-digital-garden
- [[galaxie-gd]]: https://github.com/Greaby/galaxie-gd
	- https://github.com/Greaby/telescope
	- ![[Pasted image 20220501220435.png]]
- https://jevakallio.github.io/notes/
- https://notes.binnyva.com/
	- https://github.com/binnyva/gatsby-garden
- https://www.notion.so/mindforest/818782f2ff0f44ccbc5941e3fd4d0cd0?v=3badd8762a2f424189dc13c6f4f11539
- Collector
	- https://github.com/KasperZutterman/Second-Brain
	- https://wiki.nikitavoloboev.xyz/other/wiki-workflow#similar-wikis-i-liked
	- https://github.com/RichardLitt/meta-knowledge
	- https://github.com/lyz-code/best-of-digital-gardens
	- https://github.com/kyrose/awesome-digital-gardens

- Page design siêu đẹp https://www.gwern.net/index
- https://github.com/Jekyll-Garden/jekyll-garden.github.io
- https://enjoyment-work.netlify.app/
- https://github.com/hikerpig/foam-template-gatsby-kb
	- ![[Pasted image 20220502112326.png]]
	- Có graph và interact được

## Related:
- [[Obsidian Publish]]
- [[Obsidian Forum]]