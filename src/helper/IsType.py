def is_number(s: str) -> bool:
  for i in s:
    if not (ord('0') <= ord(i) <= ord('9')):
      return False
  return True