#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-bson_ext
Version  : 1.12.3
Release  : 2
URL      : https://rubygems.org/downloads/bson_ext-1.12.3.gem
Source0  : https://rubygems.org/downloads/bson_ext-1.12.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: rubygem-bson_ext-lib
BuildRequires : ruby
BuildRequires : rubygem-bson
BuildRequires : rubygem-rdoc

%description
No detailed description available

%package lib
Summary: lib components for the rubygem-bson_ext package.
Group: Libraries

%description lib
lib components for the rubygem-bson_ext package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n bson_ext-1.12.3
gem spec %{SOURCE0} -l --ruby > rubygem-bson_ext.gemspec

%build
gem build rubygem-bson_ext.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
bson_ext-1.12.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/bson_ext-1.12.3.gem
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/CBson/cdesc-CBson.ri
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/CBson/deserialize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/CBson/max_bson_size-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/CBson/serialize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/CBson/update_max_bson_size-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/Object/valid%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/ext/cbson/page-Makefile.ri
/usr/lib64/ruby/gems/2.2.0/doc/bson_ext-1.12.3/ri/unknown/cdesc-unknown.ri
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/bson_ext-1.12.3/gem.build_complete
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/bson_ext-1.12.3/gem_make.out
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/bson_ext-1.12.3/mkmf.log
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/VERSION
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/bson_ext.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/.RUBYARCHDIR.-.bson_ext.time
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/Makefile
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/bson_buffer.c
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/bson_buffer.h
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/bson_buffer.o
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/cbson.c
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/cbson.o
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/encoding_helpers.c
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/encoding_helpers.h
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/encoding_helpers.o
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/extconf.rb
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/version.h
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/csasl/csasl.c
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/csasl/extconf.rb
/usr/lib64/ruby/gems/2.2.0/specifications/bson_ext-1.12.3.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/bson_ext-1.12.3/bson_ext/cbson.so
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/bson_ext/bson_ext/cbson.so
/usr/lib64/ruby/gems/2.2.0/gems/bson_ext-1.12.3/ext/cbson/cbson.so