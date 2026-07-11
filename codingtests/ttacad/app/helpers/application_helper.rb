# frozen_string_literal: true

# TLC
module ApplicationHelper
  # Returns the full title on a per-page basis.
  def full_title(page_title = '')
    base_title = 'The Truth About Cats and Dogs'
    if page_title.empty?
      base_title
    else
      page_title + ' | ' + base_title
    end
  end
end
