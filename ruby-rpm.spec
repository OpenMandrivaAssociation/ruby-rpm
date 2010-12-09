%define	rbname	rpm

Summary:	An interface to access RPM database for Ruby
Name:		ruby-%{rbname}
Version:	1.2.3
Release:	%mkrel 12
Group:		Development/Ruby
License:	GPL
URL:		http://rubyforge.org/projects/ruby-rpm/
Source0:	%{name}-%{version}.tar.bz2
Source1:	rpmvercmp.rb
Patch0:		ruby-rpm-1.2.3-rpm46.patch
Patch2:		ruby-rpm-1.2.3-rpm5.patch
Patch3:		ruby-rpm-1.2.3-suggests.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	ruby-devel >= 1.8.1
BuildRequires:	rpm-devel >= 4.2.1

%description
Ruby/RPM is an interface to access RPM database for Ruby

%prep
%setup -q
%patch0 -p1 -b .rpm46~
%patch2 -p1 -b .rpm5~
%patch3 -p1 -b .suggests~

%build
ruby install.rb config \
    --bin-dir=%{_bindir} \
    --rb-dir=%{ruby_sitelibdir} \
    --so-dir=%{ruby_sitearchdir} \
    --data-dir=%{_datadir}

ruby install.rb setup

%install
rm -rf %{buildroot}
ruby install.rb config \
    --bin-dir=%{buildroot}%{_bindir} \
    --rb-dir=%{buildroot}%{ruby_sitelibdir} \
    --so-dir=%{buildroot}%{ruby_sitearchdir} \
    --data-dir=%{buildroot}%{_datadir}
ruby install.rb install
chmod 0755 %{buildroot}%{ruby_sitearchdir}/rpmmodule.so
mkdir -p %{buildroot}%{_bindir}
cp -p %{SOURCE1} %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog doc
%{ruby_sitelibdir}/rpm.rb
%{ruby_sitearchdir}/rpmmodule.so
%{_bindir}/rpmvercmp.rb


