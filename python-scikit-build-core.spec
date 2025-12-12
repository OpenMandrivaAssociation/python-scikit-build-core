Name:		python-scikit-build-core
Version:	0.11.6
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/scikit-build-core/scikit_build_core-%{version}.tar.gz
Summary:	Build backend for CMake based projects
URL:		https://pypi.org/project/scikit-build-core/
License:	None
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildArch:	noarch

%description
Build backend for CMake based projects

%files
%{py_sitedir}/scikit_build_core
%{py_sitedir}/scikit_build_core-*.*-info
