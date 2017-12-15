def knot_hash_encrypt(raw_text):
    lengths_ending = [17, 31, 73, 47, 23]

    lengths = [ord(i) for i in raw_text] + lengths_ending
    nums = [x for x in range(256)]
    current_position = 0
    skip_size = 0

    for number in range(64):
        for length in lengths:
            things_to_reverse = []
            start_index_of_things_to_reverse = current_position
            for i in range(length):
                try:
                    nums[start_index_of_things_to_reverse]
                except IndexError:
                    things_to_reverse.append(nums[start_index_of_things_to_reverse - len(nums)])
                else:
                    things_to_reverse.append(nums[start_index_of_things_to_reverse])
                start_index_of_things_to_reverse += 1

            start_index_of_things_to_add = current_position
            for j in range(length):
                try:
                    nums[start_index_of_things_to_add]
                except IndexError:
                    nums[start_index_of_things_to_add - len(nums)] = things_to_reverse.pop()
                else:
                    nums[start_index_of_things_to_add] = things_to_reverse.pop()
                start_index_of_things_to_add += 1

            current_position += length + skip_size
            if current_position > len(nums):
                current_position %= len(nums)
            skip_size += 1

    sixteen_bits = []

    for i in range(16):
        section = nums[0:16]
        nums = nums[16:]

        sixteen_bits.append(section[0] ^ section[1] ^ section[2] ^ section[3] ^ section[4] ^ section[5] ^ section[6] ^ section[7] ^ section[8] ^ section[9] ^ section[10] ^ section[11] ^ section[12] ^ section[13] ^ section[14] ^ section[15])

    hexed_answer = ''

    for item in sixteen_bits:
        if len(hex(item)) == 4:
            hexed_answer += hex(item)[2:]
        else:
            hexed_answer += ('0' + hex(item)[-1])

    return hexed_answer
