use strict;
use utf8;

# Code to create section-ids from plain text is used both in mkindex and in uni.pl

sub urlify {
    my ($section)=@_;

    if($section =~ m/(.*)\[(.*)\]\(.*\).*/) {
        # The section header contains a link to somewhere else, we'll strip out the "text" portion
        # for use in the 'urlify' output
        my $old_section = $section;

        $section = "$1$2";
    }

    # Turkish character transliteration
    $section =~ s/ç/c/g;
    $section =~ s/Ç/c/g;
    $section =~ s/ğ/g/g;
    $section =~ s/Ğ/g/g;
    $section =~ s/ı/i/g;
    $section =~ s/İ/i/g;
    $section =~ s/ö/o/g;
    $section =~ s/Ö/o/g;
    $section =~ s/ş/s/g;
    $section =~ s/Ş/s/g;
    $section =~ s/ü/u/g;
    $section =~ s/Ü/u/g;

    # convert letters to lower case
    $section =~ tr/[A-Z]/[a-z]/;

    # Convert all '<' to '-less-than'
    $section =~ s/\</-less-than-/g;

    # Convert all '>' to '-greater-than'
    $section =~ s/\>/-greater-than-/g;

    # Convert all '.' to '-dot'
    $section =~ s/\./-dot-/g;

    # Convert all '/' to '-slash'
    $section =~ s/\//-slash-/g;

    # remove rubbish
    $section =~ s/[*`'":\(\),]+//g;

    # convert anything left that isn't a dash, underscore, number or letter
    $section =~ s/[^_a-zA-Z0-9-]/-/g;

    # If the starting chars aren't a letter or underscore, prepend "sect-" to them to turn them
    # into legal identifiers
    $section =~ s/^([^_a-zA-Z]+)/sect-$1/g;

    # strip trailing dash '-' characters from the section header
    $section =~ s/-+$//;

    return "$section";
}

1;
