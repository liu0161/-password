# DES 数据加密标准实验

本项目使用 Python 实现 DES（Data Encryption Standard）分组密码算法，并对 DES S 盒的若干密码学性质进行验证。代码不依赖第三方库，可直接运行。

## 文件说明

- `des_experiment.py`：DES 完整实验代码
  - DES 标准常量表
  - 比特转换和置换工具函数
  - 子密钥生成算法
  - DES `f` 函数
  - DES 加密与解密
  - S 盒密码学性质验证
  - 教材 P64 经典样例验证
  - 扩展思考题文字说明

## 运行环境

- Python 3.8 或更高版本
- 无需安装第三方依赖

## 运行方法

在当前目录执行：

```bash
python des_experiment.py
```

程序会依次运行：

1. DES 子密钥、`f` 函数、加密、解密测试
2. 8 个 S 盒的密码学性质验证
3. 教材 P64 DES 完整加密实例验证

## 主要函数

### 工具函数

- `str_to_bitlist(s)`：字符串转换为 0/1 比特列表
- `bitlist_to_str(bits)`：0/1 比特列表转换为字符串
- `hex_to_bitlist(hex_str)`：十六进制字符串转换为比特列表
- `bitlist_to_hex(bits)`：比特列表转换为十六进制字符串
- `permute(block, table)`：按 DES 置换表进行置换
- `left_shift(bits, n)`：循环左移
- `xor_bits(a, b)`：两个等长比特列表异或
- `hamming_distance(a, b)`：计算汉明距离

### DES 核心函数

- `generate_subkeys(key)`：生成 16 个 48 位轮子密钥
- `feistel_function(r, subkey)`：DES 轮函数 `f(R, K)`
- `f_function(r, subkey)`：`feistel_function` 的别名
- `des_encrypt(plaintext, key)`：DES 加密
- `des_decrypt(ciphertext, key)`：DES 解密
- `trace_des_encryption(plaintext, key)`：返回子密钥、每轮中间状态和最终密文

### S 盒验证函数

- `verify_sbox_non_linear_affine()`：验证 S 盒不是线性或仿射函数
- `verify_sbox_single_bit_avalanche()`：验证单比特输入变化造成至少 2 位输出变化
- `verify_sbox_criterion_3()`：验证 `S(x)` 与 `S(x xor 001100)` 至少 2 位不同
- `verify_sbox_criterion_4()`：验证 `S(x) != S(x xor 11yz00)`
- `verify_sbox_balance_for_fixed_input_bit()`：验证固定 1 位输入时输出 0/1 数量接近平衡
- `verify_all_sbox_properties()`：汇总验证全部 S 盒性质

## 教材 P64 样例

程序内置验证以下 DES 标准样例：

- 明文：`0x0123456789ABCDEF`
- 密钥：`0x133457799BBCDFF1`
- 预期密文：`0x85E813540F0AB405`

运行后会输出：

- `K01` 到 `K16` 共 16 个子密钥
- 每轮后的 `L_i` 和 `R_i`
- 最终密文
- 与预期密文的比对结果

验证结果应为：

```text
最终密文: 0x85E813540F0AB405
预期密文: 0x85E813540F0AB405
验证结果: 通过
```

## 简单调用示例

```python
from des_experiment import des_encrypt, des_decrypt, bitlist_to_hex

plaintext = 0x0123456789ABCDEF
key = 0x133457799BBCDFF1

cipher_bits = des_encrypt(plaintext, key)
plain_bits = des_decrypt(cipher_bits, key)

print(bitlist_to_hex(cipher_bits))
print(bitlist_to_hex(plain_bits))
```

输出：

```text
0x85E813540F0AB405
0x0123456789ABCDEF
```

## 注意事项

- DES 是 64 位分组密码，密钥输入为 64 位，其中 8 位为奇偶校验位，实际有效密钥长度为 56 位。
- 代码中的置换表位置均按 DES 标准从 1 开始，`permute` 函数内部会自动转换为 Python 的 0 开始索引。
- `des_encrypt` 和 `des_decrypt` 默认返回 64 位比特列表，可使用 `bitlist_to_hex` 转换为十六进制字符串。
- S 盒第 5 条性质中的“接近相等”使用统计阈值判断，并输出最大偏差，便于实验报告说明。
