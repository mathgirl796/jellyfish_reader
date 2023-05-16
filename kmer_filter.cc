#include <jellyfish/jellyfish.hpp>
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    std::ifstream ifs("/home/user/duanran/repo/spider-web/ref/NC_010079.k32", ios::binary);
    std::ofstream ofs("/home/user/duanran/repo/spider-web/ref/NC_010079.k32.filtered.fa", ios::binary);

    jellyfish::file_header header(ifs);
    jellyfish::mer_dna::k(header.key_len() / 2);
    binary_reader reader(ifs, &header);

    text_writer writer;
    for (int i = 0; reader.next(); i ++) {
        ofs << ">" << reader.val() << "\n" << reader.key() << "\n";
    }

    ifs.close();
    ofs.close();
    return 0;
}
