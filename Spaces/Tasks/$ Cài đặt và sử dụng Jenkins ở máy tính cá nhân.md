# Cài đặt và sử dụng Jenkins ở máy tính cá nhân
%%
- metadata
	- UID: T-210717-1047
	- tags: #created/2021/Jul/17, #tasks/todo 
	- project: [[Research Jenkins]]
	- source: https://viblo.asia/p/tim-hieu-ve-jenkins-va-cicd-eW65GbDxlDO
%%

## Note
### Cài đặt Jenkins
- [[Jenkins được viết bằng Java]], [[Cần cài Java trước khi cài Jenkins]]
	```
	wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add - sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list' sudo add-apt-repository universe sudo apt-	get update sudo apt-get install jenkins -y
	```

- Để truy cập vào Jenkins, vào browser và nhập địa chỉ http://localhost:8080
> Ở đây chúng ta còn cần phải sử dụng Github webhook để trigger những sự kiện như tạo PR hoặc merge PR, mà webhook cần phải có một public domain để hoạt động. Các bạn có thể dùng các tool để public cổng 8080 trên local thành public domain. Ví dụ như [ngrok.com](http://ngrok.com/) và làm theo hướng dẫn hoặc chạy lệnh `ssh -R 80:localhost:8080 ssh.localhost.run`.

### Cấu hình CI
Trước tiên, Jenkins cần biết được lúc nào có 1 trigger để Pull code, nó sẽ thông qua một plugin của Jenkins, ví dụ trong trường hợp repo là [[GitHub]] thì bạn phải cài [[GitHub Pull Request Builder]] 

- Bước 1: Tạo [[Webhook]] trên repo
> Tạo webhook trên repo: Vào setting webhook, chọn Add webhook. Tại payload url, điền với format sau: `<PUBLIC_DOMAIN>/ghprbhook/` ví dụ: `http:/my-domain.com/ghprbhook/`. Content type chọn application/json và thêm Secret nếu cần. Cuối cùng tại mục action chọn Issue comments và Pull requests.

- Bước 2: Cài đặt [[GitHub Pull Request Builder]] plugin
> Vào setting: _Manage Jenkins > Configure System_, Thêm credentials (username/password) của tài khoản github cho plugin.

- Bước 3: Tạo Job mới
> Tại mục Github project nhập link của repo vào đó. Tiếp theo, chọn GitHub Pull Request Builder, tích chọn "Use github hooks for build triggering". Trong mục Advance Setting..., nhập whitelist branch khi có pull request mới được tạo. Và nếu muốn thay đổi tên hiển thị trên pull request khi job chạy thì bạn có thể setting trong mục Trigger setup. Thêm action "Update commit status during build" và nhập tên hiển thị của job vào ô "Commit Status Context".

- Bước 4: Viết script [[Pipeline]] cho job.

### Cấu hình CD


## Works to finished
- [ ] Cài đặt [[Jenkins]] trên máy tính cá nhân
- [ ] Cấu hình Jenkins để chạy trên máy tính cá nhân
- [ ] Chạy thử

- [ ] Github Webhook là gì? #question❓ 
