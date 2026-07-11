# frozen_string_literal: true

require 'csv'

# Top level comment
class ApplicationController < ActionController::Base
  # @return [Object]
  def ask
    # ideal flow (pseudo code)
    # prompt user for data height, weight
    # load data for height, weight, preference
    # use input in algorithm to calculate guess
    #   One algorithm example:
    #   calculate distance data from height, weight for all entries
    #   calculate distance data for user height, weight
    #   output guess
    # prompt user to confirm guess == preference
    # record data height, weight, preference, guess

    table = CSV.parse('assets/AnimalHeightWeight.csv', headers: true,
                                                       converters: :numeric)
    x = nil
    x = table[0][0] if table[0]

    # This is the format of the data used for determining the guess
    # [sqrt((w1-w2)^2+(h1-h2)^2), 'dog|cat']
    sq_dist = [[0.44284478, 'cat'], [0.64275596, 'cat'], [0.88920134, 'cat'],
               [1.63887306, 'dog'], [1.86518967, 'dog'], [2.03619648, 'dog']]

    puts 'table:', table, x
    result = lt_gt_dist sq_dist, 1
    @print = result
    puts result

    # puts lt_gt_dist sq_dist, 84 # expects: cat
    # puts lt_gt_dist sq_dist, 85 # expects: cat
    # puts lt_gt_dist sq_dist, 88 # expects: cat
    # puts lt_gt_dist sq_dist, 89 # expects: cat
    # puts lt_gt_dist sq_dist, 91 # expects: random
    # puts lt_gt_dist sq_dist, 93 # expects: dog
    # puts lt_gt_dist sq_dist, 96 # expects: dog
    # puts lt_gt_dist sq_dist, 97 # expects: dog
    render 'layouts/application'
  end

  # @param [Object] sq_dist
  # @param [Object] target
  # @return [Object]
  def lt_gt_dist(sq_dist, target)
    # Example (poor) guess is to get next smallest/largest weight/height
    # to the input guess = if lt_animal != gt_animal then random, else lt_animal
    # In reality this is a bad way to guess. See nearest_distance below
    less_than = []
    greater_than = []
    lt_animal = ''
    gt_animal = ''
    guess = %w[dog cat].sample # set randomly, update based on results

    sq_dist.each do |element|
      if element[0] < target
        less_than << element[0]
        lt_animal = element[1]
      elsif element[0] > target
        greater_than << element[0]
        gt_animal = element[1]
      end
    end
    guess = lt_animal if gt_animal == lt_animal || gt_animal.nil?

    [less_than.max, greater_than.min, guess]
  end

  def nearest_distance
    # Note to self:
    # This line would return the most common animal in a list of animals
    # animals_selected.group_by(&:itself).values.max_by(&:size).first
    # See assets/ttacad.py for example to port
  end
end
