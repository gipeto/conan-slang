#include <iostream>
#include <slang.h>

int main()
{
  slang::IGlobalSession *outGlobalSession = nullptr;

  if (const auto result = createGlobalSession(&outGlobalSession);
      result >= 0 && outGlobalSession != nullptr) {
    std::cout << "[Success] Test package could create a global session"
              << std::endl;
    outGlobalSession->release();
    return 0;
  }

  std::cout << "[Failure] Test package could not create a global session"
            << std::endl;
  return -1;
}
