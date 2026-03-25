
nums = [1,2,3]
print(f"Lista:{nums}\nTamanho:{len(nums)}")

nums[1:] = [20, 30, 40, 50]
print(f"\nLista atualizada:{nums}\nTamanho:{len(nums)}")

#INSERT
nums.insert(1,10)
print(f"\nAdicionando '10' na posição 1 com insert(): {nums}")