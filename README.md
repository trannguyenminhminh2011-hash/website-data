# Website lưu dữ liệu — Flask + SQLite

Website mẫu không dùng thẻ HTML `<form>`. JavaScript sử dụng `fetch()` để gửi JSON đến API Flask; Flask lưu nội dung vào SQLite.

## Tệp
- `app.py`: máy chủ và API
- `templates/index.html`: giao diện và JavaScript
- `requirements.txt`: thư viện cần cài khi triển khai

## Triển khai trên Render
- Tạo GitHub repository và tải các tệp trong thư mục này lên.
- Render → New → Web Service → kết nối repository.
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

## Lưu ý dữ liệu
SQLite trên hệ thống tệp tạm thời của hosting có thể mất dữ liệu khi khởi động lại/deploy. Để giữ dữ liệu, cấu hình persistent disk và đặt biến môi trường `DATABASE_PATH` thành đường dẫn trên disk, ví dụ `/var/data/data.db`.
Bản mẫu chưa có đăng nhập/phân quyền; không dùng để lưu dữ liệu nhạy cảm hoặc mở công khai mà chưa bổ sung bảo mật.
