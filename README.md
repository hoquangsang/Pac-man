# Dự Án Pac-Man AI
Dự án triển khai trò chơi Pac-Man cổ điển với các con ma (ghosts) được điều khiển bằng các thuật toán tìm kiếm AI. Mục tiêu là lập trình các con ma để đuổi theo Pac-Man và phân tích hiệu suất của các thuật toán tìm kiếm.

## Tổng Quan
Pac-Man là một trò chơi arcade kinh điển, trong đó người chơi điều khiển nhân vật Pac-Man di chuyển trong mê cung, thu thập các chấm (dots) và tránh các con ma. Dự án này tập trung vào việc lập trình hành vi của các con ma sử dụng các thuật toán tìm kiếm để đuổi theo Pac-Man, đồng thời đánh giá hiệu suất dựa trên các chỉ số như thời gian tìm kiếm, mức sử dụng bộ nhớ và số nút mở rộng.


## Tính Năng

- Cơ chế trò chơi Pac-Man cổ điển:
+ Pac-Man di chuyển trong mê cung, thu thập chấm và tránh ma.
+ Các con ma được lập trình để đuổi theo Pac-Man.


- Các thuật toán tìm kiếm:
+ Blue Ghost (Inky): Breadth-First Search (BFS).
+ Pink Ghost (Pinky): Depth-First Search (DFS).
+ Orange Ghost (Clyde): Uniform-Cost Search (UCS).
+ Red Ghost (Blinky): A* Search (A*).

- Các chế độ trò chơi:
+ Chế độ  từng con ma (Single Ghost Mode) -> mỗi con ma sử dụng 1 thuât toán tìm kiếm khác nhau để di chuyển đến +Pac-man.
+ Chế độ tất cả các ma hoạt động đồng thời (All Ghosts Mode).
+ Chế độ chơi tương tác (Play Mode) với Pac-Man do người chơi điều khiển.


## Cài Đặt

- Sao chép dự án:
git clone https://github.com/hoquangsang/Pac-man


- Cài đặt thư viện cần thiết:
pip install pygame


- Chạy chương trình:

Đảm bảo bạn đang ở thư mục gốc của dự án (Pac-man/).
Chạy lệnh:python main.py


## Cách chơi:

- Phím mũi tên: Di chuyển Pac-Man (lên, xuống, trái, phải).
- Phím Space: Tạm dừng trò chơi/ bắt đầu chơi.
- Phím ESC: Quay lại màn hình chọn trường hợp kiểm tra (trong game) hoặc menu chính (tại màn hình chọn).
- Phím Enter: Chọn tùy chọn trong menu.


## Chi Tiết Mê Cung

Mê cung được định nghĩa trong res/mazes/maze1.txt.
Các ký hiệu:
.: Đường đi thông thường.
+: Giao điểm.
n: Nút đặc biệt.
X: Tường.
p: Chấm năng lượng (power pellet).
P: Vị trí khởi đầu của Pac-Man.

## chi tiết các level trong trò chơi:
1. Level 1: Blue Ghost (BFS):

Sử dụng Breadth-First Search để tìm đường ngắn nhất từ Blue Ghost đến Pac-Man.
Đảm bảo Pac-Man đứng yên trong chế độ kiểm tra.
Ghi lại: thời gian tìm kiếm, bộ nhớ, số nút mở rộng.


2. Level 2: Pink Ghost (DFS):

Sử dụng Depth-First Search để đuổi theo Pac-Man.
Không đảm bảo đường ngắn nhất, ưu tiên khám phá sâu.
Ghi lại các chỉ số hiệu suất tương tự.


3. Level 3: Orange Ghost (UCS):

Sử dụng Uniform-Cost Search với chi phí dựa trên khoảng cách giữa các nút.
Đảm bảo tìm đường tối ưu dựa trên chi phí.


4. Level 4: Red Ghost (A)*:

Sử dụng A* Search với hàm heuristic (khoảng cách Manhattan hoặc Euclidean).
Tối ưu hóa đường đi dựa trên chi phí và heuristic.


5. Level 5: Chạy song song:

Tất cả các ma (Blue, Pink, Orange, Red) hoạt động đồng thời.
Đảm bảo không có hai ma chiếm cùng một vị trí.


6. Level 6: Pac-Man do người chơi điều khiển:

Cho phép người chơi điều khiển Pac-Man trong khi các ma đuổi theo.
Các ma cập nhật đường đi theo thời gian thực.



