def import_file(filepath)
  result = []
  File.open(filepath, 'r') do |file|
    file.each_line do |line|
      result.append(line.chomp.split)
    end
  end
  result
end

def run_part_one(filepath)
  input = import_file(filepath).transpose
  result = 0
  input.each do |expression|
    puts "#{expression} #{result}"
    operands = expression[...-1].map(&:to_i)
    operator = expression[-1]
    result += operator == '+' ? operands.sum : operands.reduce(&:*)
  end
  puts "for #{filepath} the result is #{result}"
end

def read_as_cephalopod(filepath)
  columns = []
  File.open(filepath, 'r') do |file|
    file.each_line { |line| columns.append(line.chomp.chars) }
  end
  columns.transpose.reverse
end

def run_part_two(filepath)
  columns = read_as_cephalopod(filepath)
  result = 0
  stack = []
  columns.each do |column|
    puts "#{column} #{result}"
    next if column.all?(' ')

    stack.push(column[...-1].join.to_i)
    result += stack.sum if column[-1] == '+'
    result += stack.reduce(&:*) if column[-1] == '*'
    stack = [] if ['+', '*'].include?(column[-1])
  end
  puts "for #{filepath} the result is #{result}"
end

def part_one
  run_part_one(PATH)
  # run_part_one(PATH)
end

def part_two
  run_part_two('./PATH')
  # run_part_two('./PATH')
end

def main
  puts 'PART ONE'
  part_one
  puts 'PART TWO'
  part_two
end

main
