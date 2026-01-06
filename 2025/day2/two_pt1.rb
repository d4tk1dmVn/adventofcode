invalid_id = /\A(\d+)\1\z/
PATH =
ranges = []
total = 0
File.open(PATH, 'r') do |file|
  file.each_line do |line|
    ranges = line.split(',')
  end
end

ranges.each do |range|
  extremes = range.split('-').map(&:to_i)
  numbers = (extremes[0]..extremes[1])
  numbers.each { |number| total += number if invalid_id.match?(number.to_s) }
end

puts "total is #{total}"
