# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/githubv4
%global commit          51d7b505e2e9434db74794b52222c13253209955
%global oldgoipath      github.com/shurcooL/githubql
%global oldgoname       %gorpmname %{oldgoipath}

%global common_description %{expand:
Client library for accessing GitHub GraphQL API v4.}

%gometa

Name:           golang-github-shurcool-githubql
Version:        0
Release:        0.3%{?dist}
Summary:        Client library for accessing GitHub GraphQL API v4
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/shurcooL/graphql)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%package -n compat-%{oldgoname}-devel
Summary:    %{summary}
BuildArch:  noarch

%description -n compat-%{oldgoname}-devel
%{common_description}

This package contains compatibility glue for code that still imports the
%{oldgoipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall

install -m 0755 -vd %{buildroot}%{gopath}/src/%(dirname %{oldgoipath})
ln -s %{gopath}/src/%{goipath} %{buildroot}%{gopath}/src/%{oldgoipath}


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%files -n compat-%{oldgoname}-devel
%dir %{gopath}/src/%(dirname %{oldgoipath})
%{gopath}/src/%{oldgoipath}


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181026git51d7b50
- Bump to commit 51d7b505e2e9434db74794b52222c13253209955

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitd8297a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420gitd8297a7
- First package for Fedora

