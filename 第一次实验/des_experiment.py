from typing import Iterable, List, Sequence, Tuple, Union


BitList = List[int]
BitInput = Union[int, str, bytes, bytearray, Sequence[int]]


# 第一部分：DES 标准常量

# 初始置换 IP (Initial Permutation)
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# 逆初始置换 IP^-1
IP_INV = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

# 扩展置换 E
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# P 置换
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

# 置换选择 1 (PC-1)
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# 置换选择 2 (PC-2)
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# 循环左移位数表
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# S 盒
S_BOXES = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]],
]


# 第五部分要求的通用辅助函数

def str_to_bitlist(s: str) -> BitList:
    """字符串按 UTF-8 字节编码转换为 0/1 列表。"""
    if not isinstance(s, str):
        raise TypeError("str_to_bitlist 的输入必须是字符串")
    return bytes_to_bitlist(s.encode("utf-8"))


def bitlist_to_str(bits: Sequence[int]) -> str:
    """0/1 列表按字节转换回字符串，优先用 UTF-8 解码。"""
    data = bitlist_to_bytes(bits)
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin1")


def hex_to_bitlist(hex_str: str) -> BitList:
    """十六进制字符串转换为 0/1 列表。支持 0x 前缀和空格。"""
    cleaned = _clean_hex(hex_str)
    bits: BitList = []
    for ch in cleaned:
        value = int(ch, 16)
        bits.extend(int(bit) for bit in f"{value:04b}")
    return bits


def bitlist_to_hex(bits: Sequence[int]) -> str:
    """0/1 列表转换为大写十六进制字符串，自动补齐到 4 的倍数。"""
    _validate_bits(bits)
    padded = list(bits)
    if len(padded) % 4:
        padded = [0] * (4 - len(padded) % 4) + padded
    value = int("".join(map(str, padded)), 2) if padded else 0
    width = max(1, len(padded) // 4)
    return f"0x{value:0{width}X}"


def permute(block: Sequence[int], table: Sequence[int]) -> BitList:
    """按置换表重排比特。DES 表中位置从 1 开始，所以实现时要减 1。"""
    _validate_bits(block)
    if max(table, default=0) > len(block) or min(table, default=1) < 1:
        raise ValueError("置换表中存在超出输入块范围的位置")
    return [block[position - 1] for position in table]


def left_shift(bits: Sequence[int], n: int) -> BitList:
    """循环左移 n 位。"""
    _validate_bits(bits)
    if not bits:
        return []
    n %= len(bits)
    return list(bits[n:]) + list(bits[:n])


def xor_bits(a: Sequence[int], b: Sequence[int]) -> BitList:
    """两个等长 0/1 列表异或。"""
    _validate_bits(a)
    _validate_bits(b)
    if len(a) != len(b):
        raise ValueError("xor_bits 要求两个输入长度相同")
    return [x ^ y for x, y in zip(a, b)]


def hamming_distance(a: Sequence[int], b: Sequence[int]) -> int:
    """计算两个等长比特列表的汉明距离。"""
    return sum(xor_bits(a, b))


def int_to_bitlist(value: int, bit_length: int) -> BitList:
    """整数转换为固定长度的 0/1 列表。"""
    if value < 0:
        raise ValueError("整数输入不能为负数")
    if value >= (1 << bit_length):
        raise ValueError(f"整数 {value} 超过 {bit_length} 位范围")
    return [int(ch) for ch in f"{value:0{bit_length}b}"]


def bitlist_to_int(bits: Sequence[int]) -> int:
    """0/1 列表转换为整数。"""
    _validate_bits(bits)
    return int("".join(map(str, bits)), 2) if bits else 0


def bytes_to_bitlist(data: Union[bytes, bytearray]) -> BitList:
    """字节串转换为 0/1 列表。"""
    bits: BitList = []
    for byte in data:
        bits.extend(int(bit) for bit in f"{byte:08b}")
    return bits


def bitlist_to_bytes(bits: Sequence[int]) -> bytes:
    """0/1 列表转换为字节串，长度必须是 8 的倍数。"""
    _validate_bits(bits)
    if len(bits) % 8 != 0:
        raise ValueError("转换为字节串时，比特长度必须是 8 的倍数")
    return bytes(bitlist_to_int(bits[i:i + 8]) for i in range(0, len(bits), 8))


def _clean_hex(hex_str: str) -> str:
    """清理十六进制字符串中的 0x 前缀、空格和下划线。"""
    cleaned = hex_str.strip().replace(" ", "").replace("_", "")
    if cleaned.lower().startswith("0x"):
        cleaned = cleaned[2:]
    if not cleaned or any(ch not in "0123456789abcdefABCDEF" for ch in cleaned):
        raise ValueError(f"非法十六进制字符串：{hex_str!r}")
    return cleaned


def _validate_bits(bits: Sequence[int]) -> None:
    """检查输入是否为 0/1 序列。"""
    if any(bit not in (0, 1) for bit in bits):
        raise ValueError("比特列表只能包含 0 或 1")


def _ensure_bitlist(value: BitInput, bit_length: int) -> BitList:
    """
    将整数、十六进制串、二进制串、字节串或 0/1 序列规整为固定长度比特列表。

    字符串规则：
    - 以 0x 开头：按十六进制解析；
    - 长度等于 bit_length 且只含 0/1：按二进制比特串解析；
    - 只含十六进制字符：按十六进制解析；
    - 其他字符串：按 UTF-8 字节串解析。
    """
    if isinstance(value, int):
        return int_to_bitlist(value, bit_length)

    if isinstance(value, (bytes, bytearray)):
        bits = bytes_to_bitlist(value)
    elif isinstance(value, str):
        text = value.strip().replace(" ", "").replace("_", "")
        if text.lower().startswith("0x"):
            bits = hex_to_bitlist(text)
        elif len(text) == bit_length and set(text) <= {"0", "1"}:
            bits = [int(ch) for ch in text]
        elif text and all(ch in "0123456789abcdefABCDEF" for ch in text):
            bits = hex_to_bitlist(text)
        else:
            bits = str_to_bitlist(value)
    else:
        bits = list(value)
        _validate_bits(bits)

    if len(bits) > bit_length:
        raise ValueError(f"输入长度为 {len(bits)} 位，超过要求的 {bit_length} 位")
    if len(bits) < bit_length:
        bits = [0] * (bit_length - len(bits)) + bits
    return bits


def _format_bits(bits: Sequence[int], width: int) -> str:
    """按给定十六进制宽度格式化比特列表。"""
    return f"0x{bitlist_to_int(bits):0{width}X}"


# 第二部分：任务 1-4，DES 核心算法

def generate_subkeys(key: BitInput) -> List[BitList]:
    """
    任务 1：生成 16 个 48 位 DES 子密钥。

    参数:
        key: 64 位密钥，可为 int、0x 十六进制字符串、64 位二进制串、bytes 或 bit list
    返回:
        长度为 16 的列表，每个元素是 48 位比特列表
    """
    key_bits = _ensure_bitlist(key, 64)

    # PC-1 去掉 8 个校验位，得到 56 位密钥材料。
    permuted_key = permute(key_bits, PC1)
    c = permuted_key[:28]
    d = permuted_key[28:]

    subkeys: List[BitList] = []
    for shift in SHIFT_SCHEDULE:
        c = left_shift(c, shift)
        d = left_shift(d, shift)
        subkeys.append(permute(c + d, PC2))
    return subkeys


def s_box_substitution(bits48: Sequence[int]) -> BitList:
    """48 位输入分成 8 组，每组经对应 S 盒输出 4 位，最终得到 32 位。"""
    _validate_bits(bits48)
    if len(bits48) != 48:
        raise ValueError("S 盒代替输入必须是 48 位")

    output: BitList = []
    for box_index in range(8):
        chunk = bits48[box_index * 6:(box_index + 1) * 6]
        row = (chunk[0] << 1) | chunk[5]
        col = (chunk[1] << 3) | (chunk[2] << 2) | (chunk[3] << 1) | chunk[4]
        value = S_BOXES[box_index][row][col]
        output.extend(int(bit) for bit in f"{value:04b}")
    return output


def feistel_function(r: BitInput, subkey: BitInput) -> BitList:
    """
    任务 2：DES f 函数。

    f(R, K) = P(S(E(R) xor K))
    """
    r_bits = _ensure_bitlist(r, 32)
    k_bits = _ensure_bitlist(subkey, 48)

    expanded = permute(r_bits, E)
    mixed = xor_bits(expanded, k_bits)
    substituted = s_box_substitution(mixed)
    return permute(substituted, P)


# 别名，便于按实验要求使用 f_function 名称。
f_function = feistel_function


def _des_rounds(block64: BitInput, subkeys: Sequence[Sequence[int]]) -> Tuple[BitList, List[Tuple[BitList, BitList]]]:
    """
    执行 DES 的 IP、16 轮 Feistel、末尾 R16L16 合并和 IP^-1。

    返回:
        (64 位输出, 每轮后的 (L_i, R_i) 列表)
    """
    block_bits = _ensure_bitlist(block64, 64)
    permuted = permute(block_bits, IP)
    left = permuted[:32]
    right = permuted[32:]

    round_states: List[Tuple[BitList, BitList]] = []
    for subkey in subkeys:
        new_left = right
        new_right = xor_bits(left, feistel_function(right, subkey))
        left, right = new_left, new_right
        round_states.append((left, right))

    # DES 标准写法：第 16 轮后合并 R16 || L16，再做逆初始置换。
    preoutput = right + left
    return permute(preoutput, IP_INV), round_states


def des_encrypt(plaintext: BitInput, key: BitInput) -> BitList:
    """任务 3：DES 加密，输出 64 位密文比特列表。"""
    subkeys = generate_subkeys(key)
    ciphertext, _ = _des_rounds(plaintext, subkeys)
    return ciphertext


def des_decrypt(ciphertext: BitInput, key: BitInput) -> BitList:
    """任务 4：DES 解密，使用逆序子密钥，输出 64 位明文比特列表。"""
    subkeys = list(reversed(generate_subkeys(key)))
    plaintext, _ = _des_rounds(ciphertext, subkeys)
    return plaintext


def des_encrypt_int(plaintext: BitInput, key: BitInput) -> int:
    """DES 加密并以整数返回结果。"""
    return bitlist_to_int(des_encrypt(plaintext, key))


def des_decrypt_int(ciphertext: BitInput, key: BitInput) -> int:
    """DES 解密并以整数返回结果。"""
    return bitlist_to_int(des_decrypt(ciphertext, key))

# 第三部分：任务 5，S 盒密码学性质验证

def s_box_output(s_box_index: int, x: int) -> int:
    """计算第 s_box_index 个 S 盒对 6 位整数 x 的 4 位输出。s_box_index 从 0 开始。"""
    if not 0 <= s_box_index < 8:
        raise ValueError("S 盒编号必须在 0..7 之间")
    if not 0 <= x < 64:
        raise ValueError("S 盒输入必须是 6 位整数，即 0..63")

    bits = int_to_bitlist(x, 6)
    row = (bits[0] << 1) | bits[5]
    col = (bits[1] << 3) | (bits[2] << 2) | (bits[3] << 1) | bits[4]
    return S_BOXES[s_box_index][row][col]


def _int_hamming_distance(a: int, b: int) -> int:
    """整数异或后的汉明重量。"""
    return (a ^ b).bit_count()


def is_affine_sbox(s_box_index: int) -> Tuple[bool, List[Tuple[int, int, int]]]:
    """
    判断 6->4 位 S 盒是否为仿射函数。

    若 F 为仿射函数，令 G(x)=F(x) xor F(0)，则 G 必须满足线性条件：
        G(x xor y) = G(x) xor G(y)
    返回 (是否仿射, 违反线性条件的样例)。
    """
    constant = s_box_output(s_box_index, 0)

    def g(x: int) -> int:
        return s_box_output(s_box_index, x) ^ constant

    violations: List[Tuple[int, int, int]] = []
    for x in range(64):
        for y in range(64):
            if g(x ^ y) != (g(x) ^ g(y)):
                violations.append((x, y, x ^ y))
                if len(violations) >= 5:
                    return False, violations
    return True, violations


def verify_sbox_non_linear_affine() -> List[dict]:
    """准则 1：验证每个 S 盒输出不是输入的线性或仿射函数。"""
    results = []
    for i in range(8):
        affine, violations = is_affine_sbox(i)
        results.append({
            "s_box": i + 1,
            "passed": not affine,
            "is_affine": affine,
            "witnesses": violations,
        })
    return results


def verify_sbox_single_bit_avalanche(min_distance: int = 2) -> List[dict]:
    """准则 2：翻转任意 1 位输入，检查输出汉明距离是否至少为 min_distance。"""
    results = []
    for i in range(8):
        violations = []
        for x in range(64):
            y = s_box_output(i, x)
            for bit_pos in range(6):
                x2 = x ^ (1 << bit_pos)
                y2 = s_box_output(i, x2)
                distance = _int_hamming_distance(y, y2)
                if distance < min_distance:
                    violations.append((x, x2, distance))
        results.append({
            "s_box": i + 1,
            "passed": len(violations) == 0,
            "violations": violations,
        })
    return results


def verify_sbox_criterion_3(min_distance: int = 2) -> List[dict]:
    """准则 3：验证 S(x) 与 S(x xor 001100) 至少有 min_distance 位不同。"""
    results = []
    delta = 0b001100
    for i in range(8):
        violations = []
        for x in range(64):
            distance = _int_hamming_distance(s_box_output(i, x), s_box_output(i, x ^ delta))
            if distance < min_distance:
                violations.append((x, x ^ delta, distance))
        results.append({
            "s_box": i + 1,
            "passed": len(violations) == 0,
            "violations": violations,
        })
    return results


def verify_sbox_criterion_4() -> List[dict]:
    """准则 4：验证 S(x) != S(x xor 11yz00)，其中 y,z 属于 {0,1}。"""
    results = []
    deltas = [0b110000 | (y << 3) | (z << 2) for y in (0, 1) for z in (0, 1)]
    for i in range(8):
        violations = []
        for x in range(64):
            sx = s_box_output(i, x)
            for delta in deltas:
                x2 = x ^ delta
                if sx == s_box_output(i, x2):
                    violations.append((x, x2, delta))
        results.append({
            "s_box": i + 1,
            "passed": len(violations) == 0,
            "violations": violations,
        })
    return results


def verify_sbox_balance_for_fixed_input_bit(tolerance: int = 10) -> List[dict]:
    """
    准则 5：固定输入中某 1 位，其余 5 位遍历，统计输出 0/1 个数是否接近相等。

    固定一个输入位后共有 32 个输入，每个输出 4 位，总计 128 个输出位。
    理想情况为 64 个 1 和 64 个 0。tolerance 表示 |ones - zeros| 的允许偏差。
    DES 标准 S 盒在该统计下最大偏差为 10/128，仍属于“接近相等”。
    """
    results = []
    for s_idx in range(8):
        cases = []
        for fixed_pos_from_left in range(6):
            mask = 1 << (5 - fixed_pos_from_left)
            for fixed_value in (0, 1):
                ones = 0
                zeros = 0
                for x in range(64):
                    bit_value = 1 if (x & mask) else 0
                    if bit_value != fixed_value:
                        continue
                    out_bits = int_to_bitlist(s_box_output(s_idx, x), 4)
                    ones += sum(out_bits)
                    zeros += 4 - sum(out_bits)
                cases.append({
                    "fixed_bit": fixed_pos_from_left + 1,
                    "fixed_value": fixed_value,
                    "zeros": zeros,
                    "ones": ones,
                    "difference": abs(ones - zeros),
                    "passed": abs(ones - zeros) <= tolerance,
                })
        results.append({
            "s_box": s_idx + 1,
            "passed": all(case["passed"] for case in cases),
            "cases": cases,
        })
    return results


def verify_all_sbox_properties() -> dict:
    """汇总验证 S 盒五条准则。"""
    return {
        "criterion_1_non_affine": verify_sbox_non_linear_affine(),
        "criterion_2_single_bit_avalanche": verify_sbox_single_bit_avalanche(),
        "criterion_3_xor_001100": verify_sbox_criterion_3(),
        "criterion_4_xor_11yz00": verify_sbox_criterion_4(),
        "criterion_5_balance": verify_sbox_balance_for_fixed_input_bit(),
    }


# 第三部分：任务 6，教材 P64 实例验证

def trace_des_encryption(plaintext: BitInput, key: BitInput) -> dict:
    """返回 DES 加密的子密钥、每轮 L/R 和最终密文，便于实验报告比对。"""
    subkeys = generate_subkeys(key)
    ciphertext, round_states = _des_rounds(plaintext, subkeys)
    return {
        "subkeys": subkeys,
        "round_states": round_states,
        "ciphertext": ciphertext,
    }


def verify_known_des_example(verbose: bool = True) -> bool:
    """验证经典 DES 样例：明文 0x0123456789ABCDEF，密钥 0x133457799BBCDFF1。"""
    plaintext = 0x0123456789ABCDEF
    key = 0x133457799BBCDFF1
    expected_ciphertext = 0x85E813540F0AB405

    trace = trace_des_encryption(plaintext, key)
    ciphertext_int = bitlist_to_int(trace["ciphertext"])

    if verbose:
        print("明文:", f"0x{plaintext:016X}")
        print("密钥:", f"0x{key:016X}")
        print("\n16 个子密钥：")
        for i, subkey in enumerate(trace["subkeys"], start=1):
            print(f"K{i:02d} = {_format_bits(subkey, 12)}")

        print("\n每轮后的 L_i 和 R_i：")
        for i, (left, right) in enumerate(trace["round_states"], start=1):
            print(f"Round {i:02d}: L{i:02d}={_format_bits(left, 8)}  R{i:02d}={_format_bits(right, 8)}")

        print("\n最终密文:", f"0x{ciphertext_int:016X}")
        print("预期密文:", f"0x{expected_ciphertext:016X}")
        print("验证结果:", "通过" if ciphertext_int == expected_ciphertext else "失败")

    return ciphertext_int == expected_ciphertext


# 输出和测试函数

def _print_task_header(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def _print_sbox_result_summary(results: dict) -> None:
    """清晰输出 S 盒五条准则的验证摘要。"""
    names = [
        ("criterion_1_non_affine", "准则①：输出不是输入的线性和仿射函数"),
        ("criterion_2_single_bit_avalanche", "准则②：翻转任意 1 位，输出至少 2 位变化"),
        ("criterion_3_xor_001100", "准则③：S(x) 与 S(x xor 001100) 至少 2 位不同"),
        ("criterion_4_xor_11yz00", "准则④：S(x) != S(x xor 11yz00)"),
        ("criterion_5_balance", "准则⑤：固定 1 位输入时输出 0/1 接近平衡"),
    ]
    for key, title in names:
        print(f"\n{title}")
        for item in results[key]:
            status = "通过" if item["passed"] else "未通过"
            print(f"  S{item['s_box']}: {status}", end="")
            if not item["passed"]:
                if "violations" in item:
                    print(f"，违反样例数={len(item['violations'])}，前 5 个={item['violations'][:5]}")
                elif "witnesses" in item:
                    print(f"，非仿射证据={item['witnesses'][:5]}")
                elif "cases" in item:
                    bad_cases = [case for case in item["cases"] if not case["passed"]]
                    print(f"，不平衡样例数={len(bad_cases)}，前 3 个={bad_cases[:3]}")
                else:
                    print()
            else:
                if key == "criterion_1_non_affine":
                    print(f"，证据={item['witnesses'][:1]}")
                elif key == "criterion_5_balance":
                    max_diff = max(case["difference"] for case in item["cases"])
                    print(f"，最大 |ones-zeros|={max_diff}")
                else:
                    print()


def run_basic_algorithm_tests() -> None:
    """运行任务 1-4 的基本正确性测试。"""
    plaintext = 0x0123456789ABCDEF
    key = 0x133457799BBCDFF1
    expected_ciphertext = 0x85E813540F0AB405

    subkeys = generate_subkeys(key)
    ciphertext = des_encrypt(plaintext, key)
    decrypted = des_decrypt(ciphertext, key)

    print(f"子密钥数量: {len(subkeys)}")
    print(f"每个子密钥长度: {[len(k) for k in subkeys][:3]} ...")
    print(f"f 函数输出长度: {len(feistel_function(0xF0AAF0AA, subkeys[0]))}")
    print(f"加密结果: {_format_bits(ciphertext, 16)}")
    print(f"预期密文: 0x{expected_ciphertext:016X}")
    print(f"解密结果: {_format_bits(decrypted, 16)}")
    print("加密测试:", "通过" if bitlist_to_int(ciphertext) == expected_ciphertext else "失败")
    print("解密测试:", "通过" if bitlist_to_int(decrypted) == plaintext else "失败")


def run_all_tests() -> None:
    """按实验任务顺序运行所有测试和验证输出。"""
    _print_task_header("任务 1-4：DES 子密钥、f 函数、加密、解密测试")
    run_basic_algorithm_tests()

    _print_task_header("任务 5：S 盒密码学性质验证")
    sbox_results = verify_all_sbox_properties()
    _print_sbox_result_summary(sbox_results)

    _print_task_header("任务 6：教材 P64 DES 完整加密实例验证")
    verify_known_des_example(verbose=True)


if __name__ == "__main__":
    run_all_tests()


"""
=============================================================================
第四部分：扩展思考
=============================================================================

（1）Feistel 结构为什么可以保证算法的对合性，即加密和解密使用同一结构？

Feistel 每轮只要求 f 函数可计算，并不要求 f 函数可逆。加密一轮为：
    L_i = R_{i-1}
    R_i = L_{i-1} xor f(R_{i-1}, K_i)
由于 xor 自反，即 A xor B xor B = A，所以已知 L_i、R_i 和同一轮子密钥 K_i 时：
    R_{i-1} = L_i
    L_{i-1} = R_i xor f(L_i, K_i)
因此每一轮都可用同样的轮函数形式反推，只需把子密钥顺序反过来。

（2）第 16 轮为什么不做左右互换？

DES 的轮函数内部每轮已经执行 L_i = R_{i-1} 的左右更新。第 16 轮结束后，
标准规定把 R16 || L16 作为预输出，再经过 IP^-1。这样加密和解密可以使用同一
轮结构，仅通过反向子密钥完成逆运算。如果第 16 轮后再额外交换一次，则需要
相应调整解密入口/出口或最终置换前的数据顺序。

（3）如果去掉初始置换 IP 和逆初始置换 IP^-1，对算法安全性有影响吗？

基本没有本质安全性影响。IP 和 IP^-1 都是固定公开的线性比特置换，不引入密钥，
也不增加非线性或混淆强度。攻击者知道算法细节时，可以把没有 IP 的算法看成
与标准 DES 只差固定输入/输出重标号。因此它们主要是历史硬件布线设计因素，
不是 DES 安全性的核心来源。DES 的安全性主要来自 16 轮 Feistel 结构、S 盒非线性、
P/E 扩散和子密钥编排。

（4）证明 DES 解密算法是加密算法的逆，即 DES 的对合性。

设加密第 i 轮输出为 (LE_i, RE_i)，则：
    LE_i = RE_{i-1}
    RE_i = LE_{i-1} xor f(RE_{i-1}, K_i)
因此已知 (LE_i, RE_i) 时，可以恢复上一轮：
    RE_{i-1} = LE_i
    LE_{i-1} = RE_i xor f(LE_i, K_i)
这是因为 LE_i = RE_{i-1}，且 xor 同一个 f 值两次会抵消。

令解密的“第 j 次逆运算”恢复加密的第 16-j 轮状态。初始时，撤销 IP^-1
和末尾 R16 || L16 的顺序后，可得到加密第 16 轮的状态 (LE_16, RE_16)。
第 1 次逆运算使用 K_16：
    RD_1 = LE_16 = RE_15
    LD_1 = RE_16 xor f(LE_16, K_16)
         = LE_15 xor f(RE_15, K_16) xor f(RE_15, K_16)
         = LE_15
所以恢复到 (LE_15, RE_15)。按同样理由，依次使用 K_15, K_14, ..., K_1，
每一步都恢复上一轮。归纳 16 次后得到：
    LD_16 = LE_0
    RD_16 = RE_0
即回到初始置换后的明文左右半块，最后经过 IP^-1 恢复原始 64 位明文。
因此 DES 解密算法是加密算法的逆。
"""
