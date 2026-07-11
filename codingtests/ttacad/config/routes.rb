# frozen_string_literal: true

Rails.application.routes.draw do
  resources :preferences
  resources :people
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root 'application#ask'
  # root 'people#index'
end
