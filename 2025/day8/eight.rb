TEST_FILES = %w[./PATH].freeze
ALL_FILES = %w[./PATH ./PATH].freeze

def read_input(filepath)
  result = []
  File.open(filepath, 'r') do |file|
    file.each_line do |line|
      split = line.chomp.split(',').map(&:to_i)
      result.append(split)
    end
  end
  result
end

def distance(point_a, point_b)
  difference = []
  point_a.each_with_index do |coord, i|
    difference.append(coord - point_b[i])
  end
  difference.map { |coord| coord * coord }.sum
end

def calculate_distances(hash, point_a, other_points)
  other_points.each do |point_b|
    hash[[point_a, point_b]] = distance(point_a, point_b)
  end
end

def calculate_all_distances(input)
  result = {}
  input.each_with_index do |point, i|
    calculate_distances(result, point, input[(i + 1)..])
  end
  result
end

def connect_two_circuits(hash, circuits)
  min, max = *circuits.sort
  hash.keys.each { |key| hash[key] = min if hash[key] == max }
end

def are_in_diff_circuits?(circuits)
  return false unless circuits.none?(nil)

  circuits[0] != circuits[1]
end

def add_to_existing_circuit(result, pair)
  point_a, point_b = *pair
  circuit_a, circuit_b = pair.map { |point| result[point] }
  if circuit_a.nil?
    result[point_a] = circuit_b
  else
    result[point_b] = circuit_a
  end
end

def add_to_new_circuit(result, pair, smallest)
  pair.each { |point| result[point] = smallest }
end

def make_connections(distances, limit)
end

def calculate_relevant_connections(distances, limit)
  smallest = 0
  result = {}
  distances[..limit].each do |pair|
    circuits = pair.map { |point| result[point] }
    if are_in_diff_circuits?(circuits)
      connect_two_circuits(result, circuits)
    elsif circuits.any?
      add_to_existing_circuit(result, pair)
    else
      add_to_new_circuit(result, pair, smallest)
      smallest += 1
    end
  end
  result
end

def calculate_last_connection(distances, limit)
  smallest = 0
  aux = {}
  distances.each do |pair|
    circuits = pair.map { |point| aux[point] }
    if are_in_diff_circuits?(circuits)
      connect_two_circuits(aux, circuits)
    elsif circuits.any?
      add_to_existing_circuit(aux, pair)
    else
      add_to_new_circuit(aux, pair, smallest)
      smallest += 1
    end
    return pair if aux.keys.length == limit
  end
end

def calculate_product(connections)
  grouped = connections.group_by { |_, v| v }.values
  counted = grouped.map(&:length).sort[-3..]
  counted.reduce(&:*)
end

def run_part_one(path, distances)
  limit = path.include?('test') ? 9 : 999
  relevant_connections = calculate_relevant_connections(distances, limit)
  result = calculate_product(relevant_connections)
  puts "for file #{path}, the result is #{result}"
end

def run_part_two(path, limit, distances)
  keys = calculate_last_connection(distances, limit)
  result = keys.map { |point| point[0] }.reduce(&:*)
  puts "for file #{path}, the result should be #{result}"
end

def part_one(pairs)
  pairs.each { |path, _, distances| run_part_one(path, distances) }
end

def part_two(pairs)
  pairs.each { |triplet| run_part_two(*triplet) }
end

def main
  files = ALL_FILES
  puts 'READING FILES...'
  inputs = files.map { |path| [path, read_input(path)] }
  puts 'CALCULATING ALL DISTANCES...'
  distances = inputs.map { |path, input| [path, input.length, calculate_all_distances(input)] }
  puts 'ORDERING ALL DISTANCES...'
  distances.map! { |p, l, d| [p, l, d.keys.sort { |a, b| d[a] <=> d[b] }] }
  puts 'PART ONE'
  part_one(distances)
  puts 'PART TWO'
  part_two(distances)
end

main
