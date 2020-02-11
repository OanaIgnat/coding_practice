def nearest_multiple_10(nb):
    if nb % 10 == 0:
        print(nb)
        return
    d = int(nb / 10)
    m = nb % 10
    if m >= 5:
        print ((d + 1) * 10)
    else:
      if d == 0:
        d = d + 1
      print(d * 10)


def remove_duplicates(exp):
    l = []
    new_s = ''
    
    for i in range(len(exp)):
      if exp[i] not in l:
        l.append(exp[i])
        new_s += exp[i] # cannot do new_s[i] = ..; string does not support assignment, do instead +
      else:
        new_s += ''
    print(new_s)



def main():
  # nearest_multiple_10(10)
  # nearest_multiple_10(2)
  # nearest_multiple_10(6)
  # nearest_multiple_10(1223)
  # nearest_multiple_10(1226)
  remove_duplicates("aabbcc")
  remove_duplicates("abc")

if __name__ == "__main__":
  main()
