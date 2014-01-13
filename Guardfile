# -*- mode: ruby -*-
# More info at https://github.com/guard/guard#readme
 
require 'guard/guard'

if RUBY_PLATFORM.match('linux')
  notification :libnotify
elsif RUBY_PLATFORM.match('darwin|mac')
  notification :growl
end
 
module ::Guard
  class Pytest < ::Guard::Guard
    def run_all
      system "py.test -q tests"
    end
 
    def run_on_change(paths)
      test_files = paths.reject { |path| path.match %r{^tests/} }.inject( [] ) do |test_files, path|
        dir = File.dirname( path )
        dirs = dir.split( '/' )
        filename = File.basename( path )
        [
          "tests/#{dir}/test_#{filename}",
          "tests/test_" + ( dirs ).join( '_' ) + '_' +  filename,
          "#{dir}/test/test_#{filename}"
        ].select do |pattern|
          test_files << pattern if File.exists? pattern
        end
      end
      test_files += paths.grep( %r{^tests/} )
 
      output = `py.test -q #{test_files.join(' ')}`
      puts output
 
      # Send out a notification, via Growl (mac) or libnotify (linux).
      result_match = output.match( /\n.*seconds$/ )
      result = result_match ? result_match[0] : "unknown failure"
      image  = result.match( /fail/ ) ? :failed : :success
      project_name = File.split(Dir.getwd)[-1]
      ::Guard::Notifier.notify( result,
                                :title => "Test: " + project_name, 
                                :image => image )
    end
  end
end
 
guard :py_test do
  watch( %r{.*.py$} )
  watch( %r{^tests/.*.py$} )
  watch( 'tests/conftest.py' ) { Dir['tests/**/test*.py'] }
end