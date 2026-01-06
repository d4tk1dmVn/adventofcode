def import_file(filepath)
  matrix = []
  File.open(filepath, 'r') do |file|
    file.each_line do |line|
      matrix.append(line)
    end
  end
  matrix
end

NEIGHBOUR_OFFSETS = [
  [-1, -1], [-1, 0], [-1, 1], [0, -1],
  [0, 1], [1, -1], [1, 0], [1, 1]
].freeze

def valid_square?(coordinates, line_amount, line_length)
  result = true
  result &= coordinates[0].between?(0, line_amount - 1)
  result &= coordinates[1].between?(0, line_length - 1)
  result
end

def calculate_neighbours(alpha, beta, line_amount, line_length)
  NEIGHBOUR_OFFSETS.map { |x, y| [x + alpha, y + beta] }
                   .select { |neihgbour| valid_square?(neihgbour, line_amount, line_length) }
end

def filter_relevant_squares(matrix, relevant_char)
  result = []
  matrix.each.with_index(0) do |line, i|
    line.each_char.with_index(0) do |char, j|
      result.append([i, j]) if char == relevant_char
    end
  end
  result
end

def calculate_adjacencies(matrix, squares)
  adjacencies = {}

  squares.each do |x, y|
    neighbours = calculate_neighbours(x, y, matrix.length, matrix[0].length)
    neighbours.select! { |i, j| matrix[i][j] == matrix[x][y] }
    adjacencies[[x, y]] = neighbours.length
  end
  adjacencies
end

def run_part_one(filepath)
  original_matrix = import_file(filepath)
  relevant_squares = filter_relevant_squares(original_matrix, '@')
  adjacencies = calculate_adjacencies(original_matrix, relevant_squares)
  result = adjacencies.filter { |_, value| value < 4 }.length
  puts "The result for #{filepath} is #{result}"
end

def part_one
  run_part_one(PATH)
  run_part_one(PATH)
end

def remove_reachable_squares(matrix, removable_squares)
  removable_squares.each do |x, y|
    matrix[x][y] = '.'
  end
end

def part_two_loop(matrix)
  relevant_squares = filter_relevant_squares(matrix, '@')
  adjacencies = calculate_adjacencies(matrix, relevant_squares)
  result = adjacencies.filter { |_, value| value < 4 }
  remove_reachable_squares(matrix, result.keys)
  result.length
end

def run_part_two(filepath)
  matrix = import_file(filepath)
  result = 0
  increment = part_two_loop(matrix)
  until increment.zero?
    result += increment
    increment = part_two_loop(matrix)
  end
  puts "The result for #{filepath} is #{result}"
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
