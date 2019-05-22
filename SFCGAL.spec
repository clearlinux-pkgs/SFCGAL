#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SFCGAL
Version  : 1.3.6
Release  : 1
URL      : https://github.com/Oslandia/SFCGAL/archive/v1.3.6.tar.gz
Source0  : https://github.com/Oslandia/SFCGAL/archive/v1.3.6.tar.gz
Summary  : Wrapper around the CGAL library that intents to implement 2D and 3D operations on OGC standards models
Group    : Development/Tools
License  : GPL-2.0
Requires: SFCGAL-bin = %{version}-%{release}
Requires: SFCGAL-lib = %{version}-%{release}
Requires: SFCGAL-license = %{version}-%{release}
BuildRequires : CGAL-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : gmp-dev
BuildRequires : mpfr-dev

%description
This directory includes some backports and fixes from CGAL 4.2 and 4.3.
It is included with the CMake directive include_directories()
in order to overload system include files.

%package bin
Summary: bin components for the SFCGAL package.
Group: Binaries
Requires: SFCGAL-license = %{version}-%{release}

%description bin
bin components for the SFCGAL package.


%package dev
Summary: dev components for the SFCGAL package.
Group: Development
Requires: SFCGAL-lib = %{version}-%{release}
Requires: SFCGAL-bin = %{version}-%{release}
Provides: SFCGAL-devel = %{version}-%{release}
Requires: SFCGAL = %{version}-%{release}
Requires: SFCGAL = %{version}-%{release}

%description dev
dev components for the SFCGAL package.


%package lib
Summary: lib components for the SFCGAL package.
Group: Libraries
Requires: SFCGAL-license = %{version}-%{release}

%description lib
lib components for the SFCGAL package.


%package license
Summary: license components for the SFCGAL package.
Group: Default

%description license
license components for the SFCGAL package.


%prep
%setup -q -n SFCGAL-1.3.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558517846
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1558517846
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SFCGAL
cp LICENSE %{buildroot}/usr/share/package-licenses/SFCGAL/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sfcgal-config

%files dev
%defattr(-,root,root,-)
/usr/include/SFCGAL/Coordinate.h
/usr/include/SFCGAL/Envelope.h
/usr/include/SFCGAL/Exception.h
/usr/include/SFCGAL/Geometry.h
/usr/include/SFCGAL/GeometryCollection.h
/usr/include/SFCGAL/GeometryVisitor.h
/usr/include/SFCGAL/Kernel.h
/usr/include/SFCGAL/LineString.h
/usr/include/SFCGAL/MultiLineString.h
/usr/include/SFCGAL/MultiPoint.h
/usr/include/SFCGAL/MultiPolygon.h
/usr/include/SFCGAL/MultiSolid.h
/usr/include/SFCGAL/Point.h
/usr/include/SFCGAL/Polygon.h
/usr/include/SFCGAL/PolyhedralSurface.h
/usr/include/SFCGAL/PreparedGeometry.h
/usr/include/SFCGAL/Solid.h
/usr/include/SFCGAL/Surface.h
/usr/include/SFCGAL/Transform.h
/usr/include/SFCGAL/Triangle.h
/usr/include/SFCGAL/TriangulatedSurface.h
/usr/include/SFCGAL/Validity.h
/usr/include/SFCGAL/algorithm/BoundaryVisitor.h
/usr/include/SFCGAL/algorithm/ConsistentOrientationBuilder.h
/usr/include/SFCGAL/algorithm/area.h
/usr/include/SFCGAL/algorithm/collect.h
/usr/include/SFCGAL/algorithm/collectionExtract.h
/usr/include/SFCGAL/algorithm/collectionHomogenize.h
/usr/include/SFCGAL/algorithm/collectionToMulti.h
/usr/include/SFCGAL/algorithm/connection.h
/usr/include/SFCGAL/algorithm/convexHull.h
/usr/include/SFCGAL/algorithm/covers.h
/usr/include/SFCGAL/algorithm/difference.h
/usr/include/SFCGAL/algorithm/differencePrimitives.h
/usr/include/SFCGAL/algorithm/distance.h
/usr/include/SFCGAL/algorithm/distance3d.h
/usr/include/SFCGAL/algorithm/extrude.h
/usr/include/SFCGAL/algorithm/force2D.h
/usr/include/SFCGAL/algorithm/force3D.h
/usr/include/SFCGAL/algorithm/intersection.h
/usr/include/SFCGAL/algorithm/intersects.h
/usr/include/SFCGAL/algorithm/isValid.h
/usr/include/SFCGAL/algorithm/length.h
/usr/include/SFCGAL/algorithm/minkowskiSum.h
/usr/include/SFCGAL/algorithm/normal.h
/usr/include/SFCGAL/algorithm/offset.h
/usr/include/SFCGAL/algorithm/orientation.h
/usr/include/SFCGAL/algorithm/plane.h
/usr/include/SFCGAL/algorithm/straightSkeleton.h
/usr/include/SFCGAL/algorithm/tesselate.h
/usr/include/SFCGAL/algorithm/translate.h
/usr/include/SFCGAL/algorithm/union.h
/usr/include/SFCGAL/algorithm/volume.h
/usr/include/SFCGAL/capi/sfcgal_c.h
/usr/include/SFCGAL/config.h
/usr/include/SFCGAL/detail/ComplexComparator.h
/usr/include/SFCGAL/detail/EnvelopeVisitor.h
/usr/include/SFCGAL/detail/ForceValidityVisitor.h
/usr/include/SFCGAL/detail/GeometrySet.h
/usr/include/SFCGAL/detail/GetPointsVisitor.h
/usr/include/SFCGAL/detail/Interval.h
/usr/include/SFCGAL/detail/Point_inside_polyhedron.h
/usr/include/SFCGAL/detail/TestGeometry.h
/usr/include/SFCGAL/detail/TypeForDimension.h
/usr/include/SFCGAL/detail/algorithm/coversPoints.h
/usr/include/SFCGAL/detail/generator/building.h
/usr/include/SFCGAL/detail/generator/disc.h
/usr/include/SFCGAL/detail/generator/hoch.h
/usr/include/SFCGAL/detail/generator/sierpinski.h
/usr/include/SFCGAL/detail/graph/Edge.h
/usr/include/SFCGAL/detail/graph/GeometryGraph.h
/usr/include/SFCGAL/detail/graph/GeometryGraphBuilder.h
/usr/include/SFCGAL/detail/graph/Vertex.h
/usr/include/SFCGAL/detail/graph/algorithm/isHalfEdge.h
/usr/include/SFCGAL/detail/graph/algorithm/orientation.h
/usr/include/SFCGAL/detail/io/OsgFactory.h
/usr/include/SFCGAL/detail/io/Serialization.h
/usr/include/SFCGAL/detail/io/WktReader.h
/usr/include/SFCGAL/detail/io/WktWriter.h
/usr/include/SFCGAL/detail/polygonSetToMultiPolygon.h
/usr/include/SFCGAL/detail/tools/CharArrayBuffer.h
/usr/include/SFCGAL/detail/tools/InputStreamReader.h
/usr/include/SFCGAL/detail/tools/Log.h
/usr/include/SFCGAL/detail/tools/Registry.h
/usr/include/SFCGAL/detail/transform/AffineTransform2.h
/usr/include/SFCGAL/detail/transform/AffineTransform3.h
/usr/include/SFCGAL/detail/transform/Force2D.h
/usr/include/SFCGAL/detail/transform/ForceOrderPoints.h
/usr/include/SFCGAL/detail/transform/ForceZ.h
/usr/include/SFCGAL/detail/transform/ForceZOrderPoints.h
/usr/include/SFCGAL/detail/transform/RoundTransform.h
/usr/include/SFCGAL/detail/triangulate/ConstraintDelaunayTriangulation.h
/usr/include/SFCGAL/detail/triangulate/markDomains.h
/usr/include/SFCGAL/detail/triangulate/triangulateInGeometrySet.h
/usr/include/SFCGAL/detail/ublas.h
/usr/include/SFCGAL/export.h
/usr/include/SFCGAL/io/GeometryStreams.h
/usr/include/SFCGAL/io/ewkt.h
/usr/include/SFCGAL/io/osg.h
/usr/include/SFCGAL/io/vtk.h
/usr/include/SFCGAL/io/wkt.h
/usr/include/SFCGAL/numeric.h
/usr/include/SFCGAL/triangulate/triangulate2DZ.h
/usr/include/SFCGAL/triangulate/triangulatePolygon.h
/usr/include/SFCGAL/version.h
/usr/lib64/libSFCGAL.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSFCGAL.so.1
/usr/lib64/libSFCGAL.so.1.3.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SFCGAL/LICENSE
