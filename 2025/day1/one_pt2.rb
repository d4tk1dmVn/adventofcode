pointer = 50
zeros = 0
File.open('./one_input.txt', 'r') do |f|
  f.each_line do |line|
    sign = line[0] == 'R' ? 1 : -1
    number = line[1..].to_i
    # for every turn in-place we go over 0 exactly once
    zeros += number / 100
    # either the remainder after the in-place turns or just the same number
    number %= 100
    zeros += 1 unless (pointer + (sign * number)).between?(1, 99) || pointer.zero?
    pointer += sign * number
    pointer %= 100
  end
end

puts "ZEROS: #{zeros}"
