- dùng để tìm root node của một cạnh
- hoặc hợp nhất 2 đỉnh và làm cho nút gốc của chúng giống nhau

# Quan trọng : dùng để kiểm tra các đỉnh liên kết với nhau không, kiểm ra có cycle trong graph không...

- Implementation with Quick Find: in this case, the time complexity of the find function will be O(1)O(1). However, the union function will take more time with the time complexity of O(N)O(N).
- Implementation with Quick Union: compared with the Quick Find implementation, the time complexity of the union function is better. Meanwhile, the find function will take more time in this case.
