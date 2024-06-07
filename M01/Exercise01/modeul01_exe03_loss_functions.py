'''
•Input:
– Người dùng nhập số lượng sample (num_samples) được tạo ra (chỉ nhận integer
numbers)
– Người dùng nhập loss name (MAE, MSE, RMSE-(optional)) chỉ cần MAE và
MSE, bạn nào muốn làm thêm RMSE đều được.
•Output: Print ra loss name, sample, predict, target, loss
– loss name: là loss mà người dùng chọn
– sample: là thứ tự sample được tạo ra (ví dụ num_samples=5, thì sẽ có 5 samples và
mỗi sample là sample-0, sample-1, sample-2, sample-3, sample-4)
– predict: là số mà model dự đoán (chỉ cần dùng random tạo random một số trong range
[0,10))
– target: là số target mà momg muốn mode dự đoán đúng (chỉ cần dùng random tạo
random một số trong range [0,10))
– loss: là kết quả khi đưa predict và target vào hàm loss
– note: ví dụ num_sample=5 thì sẽ có 5 cặp predict và target.
Note: Các bạn lưu ý
•Dùng .isnumeric() method để kiểm tra num_samples có hợp lệ hay không (vd: x=’10’,
num_samples.isnumeric() sẽ trả về True ngược lại là False). Nếu không hợp lệ print
’number of samples must be an integer number’ và dừng chương trình.
•Dùng vòng lặp for, lặp lại num_samples lần. Mỗi lần dùng random modules tạo
một con số ngẫu nhiên trong range [0.0, 10.0) cho predict và target. Sau đó đưa
predict và target vào loss function và print ra kết quả mỗi lần lặp.
•Dùng random.uniform(0,10) để tạo ra một số ngẫu nhiên trong range [0,10)
•Giả xử người dùng luôn nhập đúng loss name MSE, MAE, và RMSE (đơn giảng
bước này để các bạn không cần check tên hợp lệ)
•Dùng abs() để tính trị tuyệt đối ví dụ abs(-3) sẽ trả về 3
•Dùng math.sqrt() để tính căn bậc 2
'''
from utils import MAE, MSE,RMSE, numval
import sys

if __name__=="__main__":
    loss_func_list=["MAE","MSE","RMSE"]
    loss_func=input("Input the loss functions (MAE|MSE|RMSE):")
    if loss_func.upper() not in loss_func_list:
        print(f"{loss_func} loss function is not supported")
        sys.exit()

    sample=input("Input the sample:")
    if numval(sample)!=-1:
        print(f"The sample must be an integer.")
        sys.exit()
    
    if loss_func.upper()=="MAE":
        predicts, targets, loss = MAE(int(sample))
        print(f"{loss_func} with {sample} sample, {predicts} predicts, {targets} targets, {loss} losses")

    if loss_func.upper()=="MSE":
        predicts, targets, loss = MSE(int(sample))
        print(f"{loss_func} with {sample} sample, {predicts} predicts, {targets} targets, {loss} losses")

    if loss_func.upper()=="RMSE":
        predicts, targets, loss = RMSE(int(sample))
        print(f"{loss_func} with {sample} sample, {predicts} predicts, {targets} targets, {loss} losses")
