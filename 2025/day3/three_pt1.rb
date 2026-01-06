def process_line(line)
  digits = [0, 0]
  line.each_char.with_index(1) do |digit, index|
    current_digit = digit.to_i
    if current_digit > digits[0] && index != (line.length - 1)
      digits[0] = current_digit
      digits[1] = 0
    elsif current_digit > digits[1]
      digits[1] = current_digit
    end
  end
  digits
end

total_joltage = 0
File.open(PATH, 'r') do |file|
  file.each_line do |line|
    digits = process_line(line)
    total_joltage += (digits[0] * 10) + digits[1]
  end
end

puts "total joltage: #{total_joltage}"
