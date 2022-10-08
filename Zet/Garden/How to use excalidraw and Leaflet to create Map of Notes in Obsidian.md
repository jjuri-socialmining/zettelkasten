---
title: How to use excalidraw and Leaflet to create Map of Notes in Obsidian
UID: 221008112357
created: 08-Oct-2022
tags:
  - 'created/2022/Oct/08'
  - 'howto'
aliases:
  - Hướng dẫn sử dụng excalidraw and Leaflet để tạo bản đồ ghi chú trong Obsidian
publish: False
---
## Notes:
Summary:
- [[Excalidraw Plugin]] chỉ làm công việc là export ra image file. Bạn có thể sử dụng bất cứ một hình ảnh nào có sẵn để leaflet sử dụng
- [[Obsidian Leaflet Plugin|Leaflet Plugin]] sẽ sử dụng hình ảnh ở bước 1 để người dùng tạo các marker trên đó

## Cú pháp sử dụng leaflet
Dạng đơn giản nhất

```leaflet 
id: 20221008114500
image: [[20221008114500.png]] 
```

Dạng phức tạp hơn:
```leaflet 
id: 20221008114500
image: [[20221008114500.png]] 
height: 500px 
lat: 50 
long: 50 
minZoom: 1 
maxZoom: 10 
defaultZoom: 5 
unit: meters 
scale: 1 
marker: default, 39.983334, -82.983330, [[Note]] 
darkMode: false
```

![[20221008141119 ~ Map.png]]
```leaflet 
id: 20221008141119
image: [[20221008141119 ~ Map.png]] 
height: 500px 
lat: 50 
long: 50 
minZoom: 1 
maxZoom: 10 
defaultZoom: 5 
unit: meters 
scale: 1 
darkMode: false
```

[[Leaflet sample map syntax]]

