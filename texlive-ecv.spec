%global tl_name ecv
%global tl_revision 24928

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	A fancy Curriculum Vitae class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ecv
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class provides an environment for creating a fancily laid out
tabular curriculum vitae inspired by the european curriculum vitae. The
distribution comes with a German and an English template.

