#include <slang.h>
#include <iostream>

int main() {
    slang::IGlobalSession* outGlobalSession = nullptr;
    if (const auto result = createGlobalSession(&outGlobalSession); result >= 0 && outGlobalSession != nullptr)
    {
        std::cout << "Created global session" << std::endl;
        outGlobalSession->release();
    }
}
