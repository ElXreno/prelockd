%global debug_package %{nil}

Name:           prelockd
Version:        0.9
Release:        2%{?dist}
Summary:        Lock binaries and libraries in memory to improve system responsiveness under low-memory conditions

License:        MIT
URL:            https://github.com/hakavlad/prelockd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       %{name}.sysusers

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  systemd

%description
prelockd is a daemon that locks memory mapped binaries and libraries
in memory to improve system responsiveness under low-memory conditions.


%prep
%autosetup

sed -i '
    s|install.*README.md.*||
    s|install.*MANPAGE.md.*||
    s|useradd chcon daemon-reload||
    ' Makefile


%build
# Not required


%install
%make_install \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir} \
    SYSTEMDUNITDIR=%{_unitdir}


%pre
%sysusers_create_package %{name} %{SOURCE10}


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc README.md
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %attr(755, %{name}, %{name}) %{_sharedstatedir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man8/*.8.*



%changelog
* Wed May 05 2021 ElXreno <elxreno@gmail.com> - 0.9-2
- Fix epel7 & opensuse compilation error

* Wed May 05 2021 ElXreno <elxreno@gmail.com> - 0.9-1
- Update to version 0.9

* Sun Oct 4 2020 ElXreno <elxreno@gmail.com> - 0.6-3
- Set BuildArch to noarch

* Sun Oct 4 2020 ElXreno <elxreno@gmail.com> - 0.6-2
- Add prelockd user

* Sun Oct 4 2020 ElXreno <elxreno@gmail.com> - 0.6-1
- Initial packaging

