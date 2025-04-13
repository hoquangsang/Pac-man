# 
#
#
#
---

#### Các trạng thái của ghost:
- `Scatter` (phân tán): di chuyển tới 1 trong 4 góc của mê cung. Game chúng ta sẽ bỏ qua trạng thái này vì chỉ cần ghost đuổi theo pacman.
- `Chase` (truy đuổi): trạng thái chính của Ghost. 4 Ghost sẽ cùng đi tìm Pacman. Hơi khác so với thực tế:
    - `Blinky`: Red Ghost sẽ đuổi theo Pacman (basic)
    - `Pinky`: Pink Ghost sẽ đuổi theo vị trí cách Pacman 4 ô.
    - `Inky`: Blue Ghost sẽ tìm vị trí dựa theo Blinky và Pacman...
    - `Clyde`: Orange Ghost nếu cách xa Pacman sẽ giống Blinky, nếu gần hơn 8 ô (tilesize * 8) thì sẽ đặt mục tiêu góc dưới bên trái maze (graph)
- `Freight`: lúc Pacman ăn được viên năng lượng. Lúc này Pacman có thể ăn được ghost
- `Spawn`: sau khi bị Pacman ăn, nó sẽ trở về home


