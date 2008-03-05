%define rbname rpm
%define version 1.2.3
%define release %mkrel 2

Summary: An interface to access RPM database for Ruby
Name: ruby-%{rbname}
Version: %{version}
Release: %{release}
Group: Development/Ruby
License: GPL
URL: http://rubyforge.org/projects/ruby-rpm/
Source0: %{name}-%{version}.tar.bz2
Patch0: ruby-rpm-1.2.1-rpm446.patch
Patch1: ruby-rpm-1.2.3-rpm448.patch
Patch2:	ruby-rpm-1.2.3-rpm5.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ruby-devel >= 1.8.1
BuildRequires: rpm-devel >= 4.2.1
BuildRequires: db4-devel

%description
Ruby/RPM is an interface to access RPM database for Ruby

%prep
%setup -q
%patch0 -p0 -b .446
%patch1 -p0 -b .448
%patch2 -p1 -b .rpm5

%build
ruby install.rb config \
    --bin-dir=%{_bindir} \
    --rb-dir=%{ruby_sitelibdir} \
    --so-dir=%{ruby_sitearchdir} \
    --data-dir=%{_datadir}

ruby install.rb setup

%install
[ "%{buildroot}" != "/" ] && %__rm -rf %{buildroot}
ruby install.rb config \
    --bin-dir=%{buildroot}%{_bindir} \
    --rb-dir=%{buildroot}%{ruby_sitelibdir} \
    --so-dir=%{buildroot}%{ruby_sitearchdir} \
    --data-dir=%{buildroot}%{_datadir}
ruby install.rb install
chmod 0755 %{buildroot}%{ruby_sitearchdir}/rpmmodule.so

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog doc
%{ruby_sitelibdir}/rpm.rb
%{ruby_sitearchdir}/rpmmodule.so


