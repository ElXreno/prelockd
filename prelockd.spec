%global debug_package %{nil}

Name:           prelockd
Version:        0.6
Release:        3%{?dist}
Summary:        Lock binaries and libraries in memory to improve system responsiveness under low-memory conditions

License:        MIT
URL:            https://github.com/hakavlad/prelockd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:	%{name}.sysusers

Patch10:	prelockd-rpm-drop-not-required-sections-from-install.patch

BuildArch:      noarch

BuildRequires:  systemd
#Requires:       

%description
prelockd is a daemon that locks memory mapped binaries and libraries
in memory to improve system responsiveness under low-memory conditions.


%prep
%autosetup


%build
# Not required


%install
%make_install PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir} SYSTEMDUNITDIR=%{_unitdir}


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



%changelog
* Sun Oct  4 12:53:39 +03 2020 ElXreno <elxreno@gmail.com> - 0.6-3
- Set BuildArch to noarch

* Sun Oct 4 2020 ElXreno <elxreno@gmail.com> - 0.6-2
- Add prelockd user

* Sun Oct 4 2020 ElXreno <elxreno@gmail.com> - 0.6-1
- Initial packaging

