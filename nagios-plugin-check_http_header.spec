%define		plugin	check_http_header
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check HTTP header for text
Name:		nagios-plugin-%{plugin}
Version:	0.01
Release:	0.1
License:	GPL v2
Group:		Networking
Source0:	http://exchange.nagios.org/components/com_mtree/attachment.php?link_id=2165&cf_id=24#/%{plugin}.pl
# Source0-md5:	f930e465dbd93e999058c578b158a952
Source1:	%{plugin}.cfg
URL:		http://exchange.nagios.org/directory/Plugins/Websites,-Forms-and-Transactions/check_http_header/details
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
This plugin checks HTTP header for text. It's very rare task...
Standard Nagios check_http checks only content for regexp existance.

Retrieves header of HTTP response and looks in it's output for a given
text (regexp). If the text is found returns OK, if not found returns
CRITICAL, and UNKNOWN otherwise (connection error,...) plus a brief
error description.

%prep
%setup -qcT
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
