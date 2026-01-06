def import_file(filepath)
  ranges = []
  ids = []
  got_all_ranges = false
  File.open(filepath, 'r') do |file|
    file.each_line do |line|
      if got_all_ranges
        ids.push(line.chomp.to_i)
      elsif line == "\n"
        got_all_ranges = true
      else
        ranges.append(line.chomp.split('-').map(&:to_i))
      end
    end
  end
  [ranges, ids]
end

def merge_integer_ranges(ranges)
  ranges.sort!
  result = [ranges[0]]
  ranges.each do |current_range|
    latest = result[-1]
    if current_range[0] <= latest[1]
      latest[1] = [current_range[1], latest[1]].max
    else
      result.append(current_range)
    end
  end
  result
end

def belongs_to_range?(range, integer)
  integer.between?(range[0], range[1])
end

def belongs_to_any_range?(ranges, integer)
  left = 0
  right = ranges.length - 1
  until left > right
    mid = (left + right) / 2
    return true if belongs_to_range?(ranges[mid], integer)

    left = mid + 1 if ranges[mid][1] < integer
    right = mid - 1 if ranges[mid][0] > integer
  end
  false
end

def run_part_one(filepath)
  ranges, ids = *import_file(filepath)
  merged_ranges = merge_integer_ranges(ranges)
  fresh_ingredients_amount = 0
  ids.each { |id| fresh_ingredients_amount += 1 if belongs_to_any_range?(merged_ranges, id) }
  puts "For #{filepath} the fresh ingredients amount is #{fresh_ingredients_amount}"
end

def part_one
  run_part_one(PATH)
  run_part_one(PATH)
end

def run_part_two(filepath)
  ranges, = *import_file(filepath)
  merged_ranges = merge_integer_ranges(ranges)
  fresh_ingredients_amount = merged_ranges.map do |range|
    range[1] - range[0] + 1
  end.sum
  puts "For #{filepath} the fresh ingredients amount is #{fresh_ingredients_amount}"
end

def part_two
  run_part_two(PATH)
  run_part_two(PATH)
end

def main
  part_one
  part_two
end

main
