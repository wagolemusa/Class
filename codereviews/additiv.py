class Sequence(object):
  def additive_number(self, num):
    length = len(num)
    for i in range(1, int(length / 2 + 1)):
      for j in range(1, int(( length-i) / 2 + 1)):
        f_num, s_num, others = num[:i], num[i:i+j], num[i+j:]
        if self.isValid(f_num, s_num, others):
          return True
    return False


  def isValid(self, f_num, s_num, others):
    if ((len(f_num) > 1 and f_num[0] == "0") or
    (len(s_num) > 1 and s_num[0] == "0")):
      return False
    sum_str = str(int(f_num) + int(s_num))
    if sum_str == others:
      return True
    elif others.startswith(sum_str):
      return self.isValid(s_num, sum_str, others[len(sum_str):])
    else:
      return False

print Sequence().additive_number('66121830')
print Sequence().additive_number('51123')
print Sequence().additive_number('235813')
print Sequence().additive_number('112')
