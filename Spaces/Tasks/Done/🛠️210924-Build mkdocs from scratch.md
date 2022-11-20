---
title: 🛠️210924-Build mkdocs from scratch
tags:
  - '#created/2021/Sep/24'
  - 'tasks/done'
  - '#Next'
is_done: True
publish: True
---

## Notes:
Xây dựng [[Obsidian]] website bằng [[Mkdocs]]

### Steps
1. Install [[Mkdocs]] thông qua [[Python Package Manager|pip]]
	```
	pip install mkdocs
	mkdocs new my-project 
	cd my-project
	```
	Với [[Hệ điều hành Windows|Windows OS]], lúc install nhớ lưu lại đường link của python. Sau đó add vào path để run được cmd mkdocs
	```
	C:\Users\Ngoc Diep\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts
	```
	![[20210924200929.png]]
	
	Sau khi new project, bạn sẽ được một thư mục bao gồm một file configure dạng [[YAML|yml]] và môt folder chứa những [[Markdown Language|markdown]] file sẽ dùng để generate ra file [[HTML Language|html]] sau khi build mkdocs
	```
	mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
	```
	Trong cmd promp window run `mkdocs serve` để build và tạo một server
	```
	obsidian-mkdocs-from-scratch>mkdocs serve
	INFO     -  Building documentation...
	INFO     -  Cleaning site directory
	INFO     -  Documentation built in 1.45 seconds
	INFO     -  [20:16:28] Serving on http://127.0.0.1:8000/
	```
	bật trình duyệt và vào đường link `http://127.0.0.1:8000/`
	![[20210924202037.png]]
	Đây chính là nội dung tạo ra từ file `docs/index.md`
	Giờ bạn chỉ cẩn tạo và chỉnh sửa file trong folder, các chỉnh sửa sẽ hiện lên trên trình duyệt.
	
2. Chỉnh sửa vào tạo thêm page mới nào
Tạo ra một file để check các format của mkdocs
add `requirement.in` giống [[Bluebook (digital garden)]]
Nó sẽ ra như này
![[20210924210816.png]]
3. Advance Config `mkdocs.yml` 
Site info
```
site_name: Notes garden 
site_url: https://omegakid1902.github.io/
```
Use `nav` 
```
site_name: Notes garden 
site_url: https://omegakid1902.github.io/
nav: 
    - Home: index.md 
    - About: about.md
```
![[20210924211619.png]]
![[20210924211806.png]]

Theme
The available installed themes are: `readthedocs`, `mkdoc`, bạn cần install thêm theme nếu thích
```
theme:
    name: mkdocs
    locale: en
    custom_dir: theme/
    static_templates:
        - sitemap.html
    include_sidebar: false
```
```
theme: readthedocs
```
Tham khảo theme trên wiki của makdocs trên [[GitHub]] [tại đây](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)
chọn `material` theme [repo](https://github.com/squidfunk/mkdocs-material)
```
theme:
	name: material
	custom_dir: theme
```
```
pip install mkdocs-material
```
add to `requirement.in` nhé =)
```
mkdocs
mkdocs-material
```
Kết quả
![[20210924213537.png]]

Favicon Icon
```
theme:
	name: material
	custom_dir: theme
	logo: image/favicon.ico
```

### Plugins
#### [ezlink](https://github.com/orbikm/mkdocs-ezlinks-plugin)
-   Optimized file name lookup
-   Code Block Preservation
-   File name linking (e.g. `[Text](file#anchor "title")`)
-   Absolute paths (e.g. `[Text](/link/to/file.md)`)
-   WikiLinks support (e.g. `[[Link#anchor|Link Title]]`)
```
xử được wiki link
[[index]]

[[index#Feature checking]]
dùng được cả 2 dạng
![image-1](image-1.png)
![image-1](images/image-1.png) -> thêm

[subpage](sub/pagesub.md)
[subpage](pagesub.md) -> thêm

sub/subpage.md
[[subpage]]

không xử được 
[[Đây là page 2]]

[[Đây là page 2#Header 1]]

```
#### [autolinks](https://github.com/midnightprioriem/mkdocs-autolinks-plugin/)

Install the plugin using pip:

`pip install mkdocs-autolinks-plugin`

Activate the plugin in `mkdocs.yml`:
```
plugins:
  - search
  - autolinks
```
solve sub folder link for md and image, no need absolute link
```
[Git Flow](git_flow.md)
![Avatar](avatar.png)
```
#### [roamlinks](https://github.com/Jackiexiao/mkdocs-roamlinks-plugin)
Install the plugin using pip:

`pip install mkdocs-roamlinks-plugin`

Activate the plugin in `mkdocs.yml`:
```
plugins:
  - search
  - roamlinks
```
quảng cáo:
![[20210924223901.png]]

#### [autoreflinks](https://github.com/pauloue/mkdocs-autoreflinks-plugin)
trace header dưới dạng format của markdown

#### [tooltipster-links](https://pypi.org/project/mkdocs-tooltipster-links-plugin/)
tool tip show page lên nè, set css từa lưa =)

#### [alternate-link](https://github.com/cmitu/mkdocs-altlink-plugin)
cũng không có gì
```
-   `[My Page](source-page.md)` can be written as `[My Page](source-page)`
-   `[My Page](source-page.md#Point)` can be written as `[My Page](source-page#Point)`
```
#### [section-index](https://github.com/oprypin/mkdocs-section-index)
optimize `nav`
#### [toc-sidebar](https://pypi.org/project/mkdocs-toc-sidebar-plugin/)
-> thêm content phía trên TOC -> idea thêm graphlink

#### [markdown_extensions](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions)

### Test template file
[[Mkdocs Feature checking]]

### Feature to support
- [ ] [[Backlink]] cho mỗi page
- [ ] [[Backlink graph view]] cho mỗi pages, web graphics by [[Canvas]] -> [[WebGL]]

Cơ bản được như vầy
![[20210925215725.png]]

Đã workaround cái [[Backlink graph view]]
![[20210926232347.png]]

Nghiên cứu sâu hơn về
- lib [[networkx]], [[bokeh]],... có chức năng tạo node của python
- import file html vào [[Material theme]]
- tạo graph view cho từng pages, hiện tại chỉ generate cho full site nên khá nặng. Tạo graph link từng page và thay thế cho table of content của [[material]] luôn.
- [[@2021-10-01]]: Github có repo này https://github.com/vasturiano/react-force-graph, có nhiều example chỉ, lấy về test thử bỏ vào trang của mình thui
	- https://vasturiano.github.io/react-force-graph/example/forcegraph-dependencies/