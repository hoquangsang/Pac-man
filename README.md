## Requiment

## 
####

#### Mô tả code
- Sử dụng pygame - thư viện hỗ trợ ...

- Về cơ bản, mục tiêu của game là làm cho các `entity` (thực thể), là pacman, ghost (inky, pinky, clyde, blinky) di chuyển trên cấu trúc `graph` là các `node`. Sử dụng pygame để cập nhật ví trị, xử lý `event`.
- Cách di chuyển của `ghosts`: dựa trên A.I. Cách di chuyển là giữa các node: từ `node` tới `target`. Trong khi `position` phản ánh vị trí cụ thể của nó.

#### Các trạng thái của ghost:
- `Scatter` (phân tán): di chuyển tới 1 trong 4 góc của mê cung. Game chúng ta sẽ bỏ qua trạng thái này vì chỉ cần ghost đuổi theo pacman.
- `Chase` (truy đuổi): trạng thái chính của Ghost. 4 Ghost sẽ cùng đi tìm Pacman. Hơi khác so với thực tế:
    - `Blinky`: Red Ghost sẽ đuổi theo Pacman (basic)
    - `Pinky`: Pink Ghost sẽ đuổi theo vị trí cách Pacman 4 ô.
    - `Inky`: Blue Ghost sẽ tìm vị trí dựa theo Blinky và Pacman...
    - `Clyde`: Orange Ghost nếu cách xa Pacman sẽ giống Blinky, nếu gần hơn 8 ô (tilesize * 8) thì sẽ đặt mục tiêu góc dưới bên trái maze (graph)
- `Freight`: lúc Pacman ăn được viên năng lượng. Lúc này Pacman có thể ăn được ghost
- `Spawn`: sau khi bị Pacman ăn, nó sẽ trở về home


## Game level:
#### Mức độ 1: Blue Ghost (Inky)
#### Mức độ 2: Pink Ghost (Pinky)
#### Mức độ 3: Orange Ghost (Clyde)
#### Mức độ 4: Red Ghost (Blinky)
#### Mức độ 5: Chế độ song song

1. Giải quyết vấn đề đụng độ

**Yêu cầu bài toán**: Trong trạng thái song song, đảm bảo rằng không có 2 `ghost` nào chiếm cùng một ví trị cùng một lúc.

**Giải pháp**: Để xử lý tránh đụng độ, ta phải hiểu cách di chuyển của các `ghost` trong trò chơi. Sau đó tìm ra các trường hợp cụ thể, khi nào thì **đụng độ**.
+ Đầu tiên, ta phải đảm bảo vị trí xuất phát của chúng không trùng (đụng độ).
+ Thứ hai, ta biết được rằng mê cung của chúng ta gồm nhiều node, với hình ảnh bên dưới:
[[]]
Nhận xét: Các node là vị trí giao của tất cả các đường thẳng trong mê cung. Vì vậy, các ghost sẽ đụng độ khi **khoảng cách** `position` tới `target` của chúng bằng nhau.


#### Mức độ 6: Pacman di chuyển