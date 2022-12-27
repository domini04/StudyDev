# Define pattern_search
def pattern_search(text, pattern):
  print("Looking for", pattern, "in", text)
  # Loop through the text
  for i in range(len(text)):
    # Check if the pattern matches
    if text[i:i+len(pattern)] == pattern:
      print("Pattern found at index", i)
      # Return if you find a match
      return
# N길이의 문자열에서 M길이의 패턴을 하나씩 비교하는 naive한 방법이므로 O(NM)의 시간복잡도를 가진다.

text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
# Invoke pattern_search

