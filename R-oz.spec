%global packname  oz
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0_19
Release:          2
Summary:          Plot the Australian coastline and states
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-19.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-graphics 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-graphics 

%description
Functions for plotting Australia's coastline and state boundaries.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_19-1
+ Revision: 776792
- Import R-oz
- Import R-oz

