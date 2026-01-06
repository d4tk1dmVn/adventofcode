def read_file(filepath)
  result = []
  File.open(filepath, 'r') do |file|
    file.each_line { |line| result.append(line.chomp) }
  end
  result
end

def move_to_next_row(coords)
  [coords[0] + 1, *coords[1..]]
end

def move_to_side_columns(coords)
  left = [coords[0], coords[1] - 1, coords[2..]]
  right = [coords[0], coords[1] + 1, coords[2..]]
  [left, right]
end

def calculate_new_beams(input, old_coords)
  max_col_index = input[0].length - 1
  result = move_to_side_columns(old_coords)
  result.select { |new_coords| new_coords[1].between?(0, max_col_index) }
end

def splitter?(input, coords)
  row, col = *coords[..1]
  input[row][col] == '^'
end

def calculate_splits(input, queue, new_coords)
  new_beams = calculate_new_beams(input, new_coords).select { |pair| input[pair[0]][pair[1]] == '.' }
  new_beams.each { |pair| brand_and_push(input, queue, pair) }
  new_beams.empty? ? 0 : 1
end

def brand_and_push(input, queue, coords)
  row, col = *coords
  input[row][col] = '|'
  queue.push(coords)
end

def run_part_one(filepath)
  input = read_file(filepath)
  queue = [[0, input[0].index('S')]]
  result = 0
  until queue.empty?
    new_coords = move_to_next_row(queue.shift)
    next unless new_coords[0] <= input.length - 1

    result += calculate_splits(input, queue, new_coords) if splitter?(input, new_coords)
    brand_and_push(input, queue, new_coords) unless splitter?(input, new_coords)
  end
  puts "\tfor filepath #{filepath} the beam is split #{result} times"
end

def calculate_splitters_coords(input)
  result = []
  input.each_with_index do |line, i|
    line.length.times do |j|
      result.append([i, j]) if splitter?(input, [i, j])
    end
  end
  result
end

def calculate_adjacencies(coords)
  result = {}
  coords.each_with_index do |splitter, i|
    left_adjacent = coords[i...].select { |pair| pair[1] == splitter[1] - 1 }
    right_adjacent = coords[i...].select { |pair| pair[1] == splitter[1] + 1 }
    result[splitter] = [left_adjacent[0], right_adjacent[0]]
  end
  result
end

def iterative_count(hash, coords_list)
  coords_list.each do |parent|
    children = hash[parent]
    hash[parent] = children.map { |child| child.nil? ? 1 : hash[child] }.sum
  end
  hash[coords_list[-1]]
end

def run_part_two(filepath)
  input = read_file(filepath)
  splitters_coords = calculate_splitters_coords(input)
  hash = calculate_adjacencies(splitters_coords)
  result = iterative_count(hash, splitters_coords.reverse)
  puts "\tfor filepath #{filepath} the amount of possible paths is #{result}\n"
end

def part_one
  run_part_one('./PATH')
  run_part_one('./PATH')
end

def part_two
  run_part_two('./PATH')
  run_part_two('./PATH')
end

def main
  puts 'PART ONE'
  part_one
  puts 'PART TWO'
  part_two
end

main
