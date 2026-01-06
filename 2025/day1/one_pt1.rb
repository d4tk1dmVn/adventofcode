pointer = 50
zeros = 0
File.open('./one_input.txt', 'r') do |f|
  f.each_line do |line|
    sign = line[0] == 'R' ? 1 : -1
    number = line[1..].to_i
    pointer += sign * number
    if (pointer % 100).zero?
      pointer = 0
      zeros += 1
    end
  end
end

puts "ZEROS: #{zeros}"
