EXPECTED_RESULT = 3121910778619
N = 12

def process_line(line)
  numbers = line.chars.map(&:to_i)
  digit_stack = []
  leftest_available_digit_index = 0
  N.times do |index|
    old_digit_index = numbers.length - N + index
    sliding_window = numbers[leftest_available_digit_index..old_digit_index]
    if sliding_window.empty?
      puts "\tEMPTY WINDOW"
    else
      new_digit = sliding_window.max
      leftest_available_digit_index += sliding_window.index(new_digit) + 1
      digit_stack.push(new_digit)
    end
  end
  digit_stack.join
end

def calculate_joltage(line)
  digits = process_line(line)
  digits.to_i
end

def joltage_calculator
  total_joltage = 0
  File.open(PATH, 'r') do |file|
    file.each_line do |line|
      current_line_best_joltage = calculate_joltage(line.chomp)
      total_joltage += current_line_best_joltage
    end
  end
  total_joltage
end
